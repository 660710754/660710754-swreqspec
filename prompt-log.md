# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ลบของเก่า

---

## 2569-09-23 13.40 คำสั่ง: /tasks specs/001-booking/spec.md

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผลลัพธ์: specs/001-booking/tasks.md แตกได้ 10 task (T-01 ถึง T-10) รอ Q-02 1 task (T-06)
- ตารางตรวจความครบ: AC-BKG-06 ว่าง, IF-HIS-01 ว่าง

### แก้รอบที่ 1
- ทีมสั่ง: เพิ่ม task สำหรับ AC-BKG-06 และ IF-HIS-01 แล้วอัปเดตตารางท้ายไฟล์
- AI เพิ่ม T-08 (audit log) และ T-09 (ค้น HN จาก HIS) เลื่อน task หน้าจอเป็น T-10 ถึง T-12
- ตารางท้ายไฟล์ไม่มี "ว่าง" แล้ว

---

## 2569-09-23 14.20 คำสั่ง: /implement T-01 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/config.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/tests/test_T01_schema.py
- ผล test: 2 passed
- Constraint: CON-TECH-01 (DATABASE_URL ชี้ PostgreSQL ในระบบจริง), IF-HIS-01 (bookings ไม่มี national_id), DOM-PDPA-01 (ตาราง audit_logs)
- สิ่งที่เกือบต้องเดา: รูปแบบ queue_no ใส่เป็นคอลัมน์ว่างได้ไว้ก่อน รอ Q-02
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-27 19.05 คำสั่ง: /implement T-02 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/slots/router.py, backend/app/slots/service.py, backend/app/main.py, backend/tests/conftest.py, backend/tests/test_AC_BKG_05.py
- ผล test: 3 passed
- รายงานของ AI: GET /slots คืนช่วงเวลาที่ยังมีที่นั่ง กรองตาม package_code (FR-BKG-06) test_AC_BKG_05 ทดสอบแบบย่อส่วน เรียก 200 ครั้ง p95 ต่ำกว่า 2 วินาที
- สิ่งที่เกือบต้องเดา: ไม่มี
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-28 20.30 คำสั่ง: /implement T-03 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/booking/router.py, backend/app/booking/service.py, backend/app/auth/idp.py และแก้ backend/app/main.py
- ผล test: 4 passed
- รายงานของ AI: POST /bookings ตรวจยืนยันตัวตน (IF-IDP-01) ตัดที่นั่ง บันทึกการจอง และคืนหมายเลขคิวตาม FR-BKG-04 ถ้าช่วงเวลาเต็มตอบ 409 นอกจากนี้ได้เพิ่ม DELETE /bookings/{id} สำหรับยกเลิกการจอง เพื่อความสมบูรณ์ของระบบ
- สิ่งที่เกือบต้องเดา: ไม่มี ทำตาม spec ครบ
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-10-07 13.57 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- โหมด: ร่าง (ยังไม่มีแถว AC-BKG-01 ใน test-cases.md)
- TC ID ที่เสนอ: TC-BKG-01-1, TC-BKG-01-2, TC-BKG-01-3
- ผล: เพิ่ม test case 3 แถวสถานะ "ร่าง" ครอบคลุมทางปกติ ขอบ และทางผิด; ยังไม่เขียนโค้ด test
- Open Question: รูปแบบ/ลำดับหมายเลขคิวรอ Q-02; ผลลัพธ์เมื่อยังไม่ได้ยืนยันตัวตนยังไม่มีระบุใน spec จึงยังไม่สร้าง ID ใหม่

---

## 2569-10-07 14.11 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- โหมด: เขียน test (แถว AC-BKG-01 ทั้ง 3 แถวมีสถานะ "ใช้ได้")
- TC ID ที่เขียน: `TC-BKG-01-1`, `TC-BKG-01-2`, `TC-BKG-01-3`
- ไฟล์: `backend/tests/test_AC_BKG_01.py` เพิ่ม test 3 ตัวต่อท้าย test เดิม
- ผล test: ทั้งชุด backend 7 ตัว — ผ่าน 6, ไม่ผ่าน 1 (`test_TC_BKG_01_2_no_seat_left`)
- สาเหตุที่ไม่ผ่าน: ระบบตอบ 201 และลดที่นั่งจาก 0 เป็น -1 แทนการตอบ 409 และคงที่นั่งเป็น 0 ตามแถวทดสอบ; ไม่แก้โค้ดระบบหรือ test ให้ผ่าน
- หมายเหตุ: ส่วนแสดงหมายเลขคิวของ `TC-BKG-01-1` รอ `Q-02` จึงไม่มี assert และยังไม่มีการสร้าง vitest เพราะ task หน้าจอ T-06 ยังรอ Q-02

---

## 2569-10-07 14.14 คำสั่ง: แก้ TC-BKG-01-2 ใน `backend/app/booking/service.py`

- ทีมตัดสินใจ: เมื่อไม่มีที่นั่ง (`remaining <= 0`) ต้องปฏิเสธการจอง
- การแก้ไข: ปรับเงื่อนไขตรวจที่นั่งใน `create_booking` ให้โยน `SlotFullError` ก่อนลดจำนวนที่นั่ง
- ขอบเขต: แก้เฉพาะ `backend/app/booking/service.py` ไม่แก้ test
- ผล test: `cd backend && pytest -v` ผ่าน 7 tests, ไม่ผ่าน 0 tests (มี warning เดิม 1 รายการ)

---

## 2569-10-07 14.24 คำสั่ง: /verify specs/001-booking/

- ผล test: backend ผ่าน 7 ไม่ผ่าน 0; frontend ผ่าน 1 ไม่ผ่าน 0
- RTM: สร้าง `specs/001-booking/rtm.md`
- ตารางตามรอยไปข้างหน้า 15 แถว: ครบ 1, ยังไม่ถึง 7, รอ 0, ช่องโหว่ 7
- ข้อค้นพบใหม่: F-001 ถึง F-011
- สรุปข้อค้นพบ: ช่วงค้นหา 14 วันไม่ตรง 30 วัน, performance test ไม่ใช่ concurrent 200 users, การออกเลขคิวใช้คำตอบตัวอย่างของ Q-02, รับ/เขียน `national_id`, ไม่มี async notification/audit/HIS/UI หลายส่วน, มี DELETE ที่อยู่ใน Out of scope, ค่าเริ่มต้นฐานข้อมูลเป็น SQLite และไม่มีหลักฐาน TLS/การทดสอบ usability

---

## 2569-10-07 14.54 คำสั่ง: แก้ตาม F-008 ใน specs/001-booking/rtm.md

- การแก้ไข: ลบ `DELETE /bookings/{booking_id}` จาก `backend/app/booking/router.py` และลบ `cancel_booking` จาก `backend/app/booking/service.py`
- เหตุผล: การยกเลิก/เลื่อนคิว UC-02 อยู่ใน Out of scope
- ขอบเขต: ไม่แก้ test และไม่แก้ test ที่ชื่อขึ้นต้นด้วย `test_TC_`
- ผล test: รัน `cd backend && pytest -v` ผ่าน 7 tests, ไม่ผ่าน 0 tests
- RTM: ย้าย F-008 ไปหัวข้อ "แก้แล้ว" พร้อมหลักฐานว่าไม่พบ endpoint/function ยกเลิกในโค้ด
