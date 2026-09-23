# Tasks: จองคิวตรวจสุขภาพ (Booking)

- Feature: จองคิวตรวจสุขภาพ (Booking)
- Spec ID: SPEC-BKG-001
- อ้างอิง plan.md: specs/001-booking/plan.md
- วันที่: 2569-09-23

## สรุป
- งานทั้งหมด: 12 task
- รอ Open Questions: 1 task (Q-02)

## รายการ task

### T-01 สร้างโครงฐานข้อมูลและ migration
- รองรับ: CON-TECH-01, DOM-PDPA-01, IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-xx
- ไฟล์ที่แตะ: backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: migration สร้างตาราง slots, bookings และ audit_logs ได้ และ test ใช้ SQLite ในหน่วยความจำทำงานร่วมกับ PostgreSQL schema ได้
- สถานะ: พร้อมทำ

### T-02 สร้าง API GET /slots และคำนวณช่วงว่าง
- รองรับ: FR-BKG-01, FR-BKG-06, NFR-PERF-01
- ตรวจด้วย: AC-BKG-05
- ไฟล์ที่แตะ: backend/app/slots/router.py, backend/app/slots/service.py, backend/tests/test_slots.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: GET /slots คืนรายการช่วงเวลาและจำนวนที่นั่งคงเหลือได้ และวัด p95 ตามเงื่อนไขของ AC-BKG-05 ผ่านในสภาพทดสอบ
- สถานะ: พร้อมทำ

### T-03 ตรวจยืนยันตัวตนก่อนเข้าถึงการจอง
- รองรับ: IF-IDP-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-xx
- ไฟล์ที่แตะ: backend/app/auth/idp.py, backend/app/main.py, backend/app/booking/router.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: ทุก endpoint ที่เกี่ยวข้องกับการจองตรวจสภาพยืนยันตัวตนก่อนให้อ่านหรือจองข้อมูลได้
- สถานะ: พร้อมทำ

### T-04 สร้าง API POST /bookings สำหรับการจองสำเร็จ
- รองรับ: FR-BKG-04, IF-HIS-01
- ตรวจด้วย: AC-BKG-01
- ไฟล์ที่แตะ: backend/app/booking/router.py, backend/app/booking/service.py, backend/tests/test_booking.py
- ต้องทำหลัง: T-01, T-02, T-03
- เสร็จเมื่อ: test_AC_BKG_01 ผ่าน และเมื่อยืนยันการจองแล้วมีการบันทึก booking, ตัดจำนวนที่นั่งลงเหลือ 0 และแสดงหมายเลขคิว
- สถานะ: พร้อมทำ

### T-05 ป้องกันการจองซ้ำในวันเดียวกัน
- รองรับ: FR-BKG-02
- ตรวจด้วย: AC-BKG-02
- ไฟล์ที่แตะ: backend/app/booking/service.py, backend/tests/test_booking.py
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: test_AC_BKG_02 ผ่าน และระบบปฏิเสธการจองซ้ำโดยคืน booking เดิมพร้อมข้อผิดพลาด 409
- สถานะ: พร้อมทำ

### T-06 คำนวณช่วงที่ใกล้เคียงเมื่อ slot เต็ม
- รองรับ: FR-BKG-03
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: backend/app/slots/service.py, backend/app/booking/service.py, backend/tests/test_booking.py
- ต้องทำหลัง: T-02, T-04
- เสร็จเมื่อ: test_AC_BKG_03 ผ่าน พร้อมข้อมูล 3 ตัวเลือกที่ใกล้ที่สุดภายในวันเดียวกันและวันถัดไป และไม่มีการจองซ้อนเกิดขึ้น
- สถานะ: พร้อมทำ

### T-07 จัดการคิวส่งข้อความและ Retry เมื่อส่งไม่สำเร็จ
- รองรับ: IF-NOT-01, FR-BKG-05, NFR-REL-02, ASM-03
- ตรวจด้วย: AC-BKG-04
- ไฟล์ที่แตะ: backend/app/notify/queue.py, backend/app/booking/service.py, backend/tests/test_notify.py
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: เมื่อระบบแจ้งเตือนไม่ตอบสนอง การจองยังบันทึกและมีงาน retry ในคิวที่กำหนดส่งภายใน 5 นาที
- สถานะ: พร้อมทำ

### T-08 บันทึก audit log และเชื่อม HIS lookup
- รองรับ: DOM-PDPA-01, IF-HIS-01
- ตรวจด้วย: AC-BKG-06
- ไฟล์ที่แตะ: backend/app/audit/middleware.py, backend/app/his/client.py, backend/tests/test_audit.py
- ต้องทำหลัง: T-01, T-03, T-04
- เสร็จเมื่อ: test_AC_BKG_06 ผ่าน โดยมี audit log ที่ระบุ actor_id, accessed_at และ hn และไม่เก็บเลขบัตรประชาชนในตารางการจอง
- สถานะ: พร้อมทำ

### T-09 สร้างหน้าเลือกแพ็กเกจและช่วงเวลา
- รองรับ: FR-BKG-01, FR-BKG-06
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-xx
- ไฟล์ที่แตะ: frontend/src/pages/SlotPicker.jsx, frontend/src/api/client.js, frontend/src/App.jsx
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: ผู้ใช้เลือกแพ็กเกจและช่วงเวลาจะโหลดข้อมูลจาก API จำลองตามสัญญาใน plan.md ได้ และเปลี่ยนแพ็กเกจแล้วมีช่วงเวลาว่างใหม่ตามตัวเลือก
- สถานะ: พร้อมทำ

### T-10 สร้างหน้้ายืนยันและแสดงช่วงเวลาเต็มพร้อม 3 ตัวเลือก
- รองรับ: FR-BKG-03
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: frontend/src/pages/ConfirmBooking.jsx, frontend/src/__tests__/AC-BKG-03.test.jsx
- ต้องทำหลัง: T-06, T-09
- เสร็จเมื่อ: test หน้าแสดงข้อความ “ช่วงเวลาเต็ม” และ 3 ตัวเลือกที่ใกล้เวลาที่เลือกที่สุดในวันเดียวกันและวันถัดไป
- สถานะ: พร้อมทำ

### T-11 ต่อหน้าจอกับ API จริงและแสดงผลการจอง
- รองรับ: FR-BKG-04, FR-BKG-05
- ตรวจด้วย: AC-BKG-01, AC-BKG-04
- ไฟล์ที่แตะ: frontend/src/pages/BookingResult.jsx, frontend/src/api/client.js, frontend/src/App.jsx
- ต้องทำหลัง: T-04, T-07, T-09, T-10
- เสร็จเมื่อ: หน้าแสดงหมายเลขคิวได้ทันที และเมื่อส่งข้อความไม่สำเร็จยังคงแสดงหมายเลขคิวที่ถูกบันทึกไว้
- สถานะ: พร้อมทำ

### T-12 เตรียมการออกหมายเลขคิวตามคำตอบ Q-02
- รองรับ: FR-BKG-04, Q-02
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-xx
- ไฟล์ที่แตะ: backend/app/db/models.py, backend/app/booking/service.py
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: ทีมตอบ Q-02 แล้วจึงกำหนดรูปแบบและอัลกอริทึมการออกหมายเลขคิวให้สอดคล้องกับเงื่อนไขที่สรุปใหม่
- สถานะ: รอ Q-02

## ตารางตรวจความครบ

### AC ID | task ที่ตรวจ AC นี้
| AC ID | task ที่ตรวจ AC นี้ |
|---|---|
| AC-BKG-01 | T-04, T-11 |
| AC-BKG-02 | T-05 |
| AC-BKG-03 | T-06, T-10 |
| AC-BKG-04 | T-07, T-11 |
| AC-BKG-05 | T-02 |
| AC-BKG-06 | T-08 |

### Constraint ID | task ที่ทำให้เป็นจริง
| Constraint ID | task ที่ทำให้เป็นจริง |
|---|---|
| CON-TECH-01 | T-01, T-02, T-04 |
| DOM-PDPA-01 | T-01, T-08 |
| IF-IDP-01 | T-03 |
| IF-HIS-01 | T-04, T-08 |
| IF-NOT-01 | T-07 |

## สิ่งที่ยังไม่ทำ
- Q-02 หมายเลขคิวรีเซ็ตรายวัน หรือนับต่อเนื่อง และมีรูปแบบอย่างไร (เช่น A001)?
  -> ถามเจ้าหน้าที่เวชระเบียน (ยังไม่ได้คำตอบ)
  -> รอ task: T-12

- Q-01 ตอบแล้ว: "ช่วงเวลาใกล้เคียง" รวมวันถัดไป 1 วัน (พยาบาลคัดกรอง 2569-09-16)
  -> ใช้แล้วใน FR-BKG-03 และไม่มี task รอเพิ่มเติม
