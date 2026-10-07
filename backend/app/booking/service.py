# บันทึกการจองและตัดที่นั่ง (T-03)
# รองรับ FR-BKG-04
from sqlalchemy.orm import Session

from app.db.models import Booking, Slot


class SlotFullError(Exception):
    """ช่วงเวลาที่เลือกไม่มีที่นั่งเหลือแล้ว"""


class DuplicateBookingError(Exception):
    """ผู้รับบริการมีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน"""

    def __init__(self, booking: Booking):
        self.booking = booking


def create_booking(db: Session, hn: str, slot_id: int) -> Booking:
    """ยืนยันการจอง: กันจองซ้ำวันเดียวกัน ตัดที่นั่ง และบันทึก (FR-BKG-02, FR-BKG-04)"""
    slot = db.get(Slot, slot_id)
    if slot is None:
        raise ValueError("ไม่พบช่วงเวลา")
    existing_booking = (
        db.query(Booking)
        .filter(
            Booking.hn == hn,
            Booking.booking_date == slot.slot_date,
            Booking.status == "BOOKED",
        )
        .first()
    )
    if existing_booking is not None:
        raise DuplicateBookingError(existing_booking)
    if slot.remaining <= 0:
        raise SlotFullError(slot_id)

    slot.remaining -= 1
    booking = Booking(
        hn=hn,
        slot_id=slot.id,
        booking_date=slot.slot_date,
        queue_no=None,  # รอ Q-02
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking
