# Tests for T-04: reject duplicate booking on the same day
# AC-BKG-02 (FR-BKG-02)
from tests.conftest import AUTH
from app.db.models import Booking


def test_TC_BKG_02_1_reject_duplicate_day(client, db, make_slot):
    # Given: ผู้รับบริการยืนยันตัวตนแล้ว และมีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน
    existing_slot = make_slot(start="08:00", remaining=1)
    existing_booking = Booking(
        hn="0001234",
        slot_id=existing_slot.id,
        booking_date=existing_slot.slot_date,
        status="BOOKED",
    )
    db.add(existing_booking)
    db.commit()
    new_slot = make_slot(start="09:00", remaining=1)

    # When: จองคิวใหม่ในวันเดียวกัน
    res = client.post("/bookings", json={"slot_id": new_slot.id}, headers=AUTH)

    # Then: ปฏิเสธการจอง
    assert res.status_code == 409
    assert db.query(Booking).count() == 1
    # Then: แสดงหมายเลขคิวเดิม (รอ Q-02) — ยังไม่ตรวจจนกว่าจะได้คำตอบ Q-02


def test_TC_BKG_02_2_allow_different_day(client, db, make_slot):
    # Given: ผู้รับบริการยืนยันตัวตนแล้ว และมีคิวที่ยังไม่ได้ใช้ แต่เป็นคนละวันกับวันที่กำลังจะจอง
    existing_slot = make_slot(start="08:00", remaining=1)
    existing_booking = Booking(
        hn="0001234",
        slot_id=existing_slot.id,
        booking_date=existing_slot.slot_date,
        status="BOOKED",
    )
    db.add(existing_booking)
    db.commit()
    new_slot = make_slot(start="09:00", remaining=1, days_from_today=2)

    # When: จองคิวในวันใหม่ที่มีที่นั่งว่าง
    res = client.post("/bookings", json={"slot_id": new_slot.id}, headers=AUTH)

    # Then: จองได้สำเร็จ
    assert res.status_code == 201
    # Then: สร้างการจองใหม่ 1 รายการ โดยการจองเดิมยังคงอยู่
    assert db.query(Booking).count() == 2


def test_TC_BKG_02_3_create_new_booking(client, db, make_slot):
    # Given: ผู้รับบริการยืนยันตัวตนแล้ว และไม่มีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน
    new_slot = make_slot(start="09:00", remaining=1)

    # When: จองคิวใหม่ในวันเดียวกัน
    res = client.post("/bookings", json={"slot_id": new_slot.id}, headers=AUTH)

    # Then: จองได้ตามปกติ
    assert res.status_code == 201
    # Then: สร้างการจองใหม่ 1 รายการ
    assert db.query(Booking).count() == 1
