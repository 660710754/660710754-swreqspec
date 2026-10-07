# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 14.24 | test: backend 7 ผ่าน 0 ไม่ผ่าน, frontend 1 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 | T-02 เสร็จ | [slots/service.py: list_available_slots](/workspaces/660710754-swreqspec/backend/app/slots/service.py:11), [slots/router.py: get_slots](/workspaces/660710754-swreqspec/backend/app/slots/router.py:12) | `test_AC_BKG_05` ผ่าน แต่ตรวจเพียง status และ p95 ไม่ตรวจช่วง 30 วัน/จำนวนที่นั่ง | ช่องโหว่ |
| FR-BKG-02 | AC-BKG-02 | T-04 พร้อมทำ | ไม่มีโค้ดหรือ test ของ AC-BKG-02 | ไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05/T-11/T-12 พร้อมทำ | ไม่มีโค้ดหรือ test ของ AC-BKG-03 | ไม่มี | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03 เสร็จ, T-06 รอ Q-02 | [booking/service.py: create_booking](/workspaces/660710754-swreqspec/backend/app/booking/service.py:22), [booking/router.py: create_booking](/workspaces/660710754-swreqspec/backend/app/booking/router.py:20) | `test_TC_BKG_01_1_last_seat` และ `test_TC_BKG_01_2_no_seat_left` ผ่านสำหรับการบันทึก/ตัดที่นั่ง; ไม่มี assert หมายเลขคิวและไม่มีการตรวจคำขอข้อความ | ช่องโหว่ |
| FR-BKG-05 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีโค้ดหรือ test ของการส่งข้อความ/คิวส่งซ้ำ | ไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02 เสร็จ, T-10 พร้อมทำ | [slots/service.py: list_available_slots](/workspaces/660710754-swreqspec/backend/app/slots/service.py:11) กรอง `package_code` | ไม่มี test การเปลี่ยนแพ็กเกจ; ไม่มี AC สำหรับ FR นี้ | ช่องโหว่ |
| NFR-PERF-01 | AC-BKG-05 | T-02 เสร็จ | [test_AC_BKG_05.py:test_AC_BKG_05](/workspaces/660710754-swreqspec/backend/tests/test_AC_BKG_05.py:6) วัด request แบบเรียงลำดับ | `test_AC_BKG_05` ผ่าน แต่ไม่จำลองผู้ใช้พร้อมกัน 200 คนตาม NFR | ช่องโหว่ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มีการตั้งค่า TLS ในโค้ด/API หรือ frontend proxy | ไม่มี | ช่องโหว่ |
| NFR-REL-02 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีโค้ดคิวส่งข้อความ/ส่งซ้ำ | ไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มีการทดสอบผู้ใช้ใหม่ 10 คนและเกณฑ์ 8 ใน 10 | ไม่มี | ช่องโหว่ |
| CON-TECH-01 | ไม่มี AC ตรง ๆ | T-01 เสร็จ | [config.py](/workspaces/660710754-swreqspec/backend/app/config.py) ใช้ PostgreSQL ได้เมื่อกำหนด env แต่ค่าเริ่มต้นเป็น SQLite | `test_T01_tables_created` ผ่านบน SQLite ไม่ยืนยัน PostgreSQL ตาม constraint | ช่องโหว่ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 พร้อมทำ | ไม่มี middleware/audit log ที่ใช้งานจริง | ไม่มี | ยังไม่ถึง |
| IF-IDP-01 | AC-BKG-01 | T-03 เสร็จ | [auth/idp.py: get_verified_hn](/workspaces/660710754-swreqspec/backend/app/auth/idp.py:7) บังคับ Authorization ก่อน POST /bookings | `test_TC_BKG_01_3_not_verified` ผ่าน | ครบ |
| IF-HIS-01 | ไม่มี AC ตรง ๆ | T-01 เสร็จ, T-09 พร้อมทำ | ไม่มี `patients/lookup` หรือ HIS client; bookings เก็บ HN และไม่มีคอลัมน์ `national_id` | `test_T01_no_national_id` ผ่านเฉพาะ schema | ยังไม่ถึง |
| IF-NOT-01 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีการ enqueue ข้อความแบบ asynchronous | ไม่มี | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| [slots/router.py: GET /slots](/workspaces/660710754-swreqspec/backend/app/slots/router.py:12) | FR-BKG-01, FR-BKG-06 | บางส่วน | คืนช่วงว่างและกรองแพ็กเกจ แต่ service จำกัดช่วงเป็น 14 วัน ไม่ใช่ 30 วัน และไม่มีหน้าจอใช้งานจริง |
| [slots/service.py: list_available_slots](/workspaces/660710754-swreqspec/backend/app/slots/service.py:11) | FR-BKG-01, FR-BKG-06 | ตรงในขอบเขตวันที่ | `DAYS_AHEAD = 30` ตรงกับช่วง 30 วันตาม FR-BKG-01 แต่ยังไม่มี test ตรวจขอบเขตวันที่และจำนวนที่นั่ง |
| [booking/router.py: POST /bookings](/workspaces/660710754-swreqspec/backend/app/booking/router.py:20) | FR-BKG-04, IF-IDP-01 | ไม่ตรงทั้งหมด | รับ `national_id` และเขียนลง log ทั้งที่ IF-HIS-01 ห้ามเก็บเลขบัตรประชาชนโดยไม่จำเป็น; ไม่ส่งข้อความยืนยัน |
| [booking/service.py: create_booking](/workspaces/660710754-swreqspec/backend/app/booking/service.py:22) | FR-BKG-04 | ไม่ตรงทั้งหมด | ทำ booking/ตัดที่นั่งและสร้าง queue number แต่รูปแบบ `A001` เป็นการตัดสินใจขณะ Q-02 ยังเปิดอยู่ และไม่มี message enqueue |
| [auth/idp.py: get_verified_hn](/workspaces/660710754-swreqspec/backend/app/auth/idp.py:7) | IF-IDP-01 | ตรงบางส่วน | จำลอง token prefix ภายในระบบ ไม่ได้เชื่อมผลจากระบบ IDP จริง; เหมาะกับ task ที่ทำอยู่แต่ยังไม่ใช่ integration จริง |
| [config.py: DATABASE_URL](/workspaces/660710754-swreqspec/backend/app/config.py:4) | CON-TECH-01 | ไม่ตรงค่าเริ่มต้น | ค่าเริ่มต้นเป็น SQLite แม้ระบบจริงกำหนด PostgreSQL |
| [frontend/src/App.jsx: App](/workspaces/660710754-swreqspec/frontend/src/App.jsx:4) | Goal, FR-BKG-01 ถึง FR-BKG-06 | ยังไม่ตรง | เป็นเพียงหน้าจอโครง ไม่มี SlotPicker, ConfirmBooking หรือ BookingResult |
| [frontend/src/api/client.js: api](/workspaces/660710754-swreqspec/frontend/src/api/client.js:5) | FR-BKG-01, FR-BKG-04 | บางส่วน | มี client แต่ไม่มีหน้าจอเรียกใช้ และไม่จัดการผลลัพธ์/ข้อความตาม AC |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง

ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-002 | test อ่อน | [test_AC_BKG_05.py:6](/workspaces/660710754-swreqspec/backend/tests/test_AC_BKG_05.py:6) | NFR-PERF-01 | วัด 200 request แบบเรียงลำดับ ไม่ใช่ผู้ใช้พร้อมกัน 200 คน จึงยืนยัน NFR ไม่ได้ | แก้โค้ด: ปรับ test ให้จำลองผู้ใช้พร้อมกัน 200 คน เพื่อให้ตรวจ NFR-PERF-01 ได้จริง |
| F-003 | AC ไม่มี test | [booking/service.py:22](/workspaces/660710754-swreqspec/backend/app/booking/service.py:22) | FR-BKG-04, AC-BKG-01 | ไม่มี assert หมายเลขคิวเพราะ Q-02 และไม่มี test การส่งคำขอข้อความ แม้ FR ระบุว่าต้องทำทั้งสองอย่าง | เพิ่ม Q-xx: ต้องตอบ Q-02 เรื่องรูปแบบหมายเลขคิวก่อน จึงจะเพิ่ม assertion หมายเลขคิวได้ครบ |
| F-004 | โค้ดไม่มี FR | [booking/router.py:22](/workspaces/660710754-swreqspec/backend/app/booking/router.py:22) | FR-BKG-04, IF-NOT-01 | การจองไม่ enqueue คำขอ SMS/LINE แบบ asynchronous ตาม requirement | แก้โค้ด: เพิ่มการ enqueue คำขอส่งข้อความแบบ asynchronous ตาม FR-BKG-04 และ IF-NOT-01 |
| F-005 | FR ไม่มี AC | [spec.md](/workspaces/660710754-swreqspec/specs/001-booking/spec.md) | FR-BKG-06 | FR-BKG-06 ไม่มี AC ตรวจการเปลี่ยนแพ็กเกจ และไม่มี test ที่ตรวจจริง | แก้ spec: เพิ่ม AC สำหรับ FR-BKG-06 เพื่อให้ตรวจสอบการเปลี่ยนแพ็กเกจและสร้าง test ได้ |
| F-006 | ละเมิด Constraint | [booking/router.py:19](/workspaces/660710754-swreqspec/backend/app/booking/router.py:19) | IF-HIS-01 | request รับ `national_id` และ logger เขียนค่า `national_id` ทั้งที่ข้อมูลบัตรประชาชนต้องไม่ถูกเก็บ/เผยโดยไม่จำเป็น | แก้โค้ด: ไม่รับและไม่เขียน `national_id` ลง log ให้ใช้ HN ตาม IF-HIS-01 |
| F-007 | เดา Q-xx | [booking/service.py:14](/workspaces/660710754-swreqspec/backend/app/booking/service.py:14) | Q-02 | กำหนดรูปแบบและลำดับ queue เป็น `A001` ทั้งที่ Q-02 ยังไม่มีคำตอบ | เพิ่ม Q-xx: ต้องตอบ Q-02 ก่อนกำหนดรูปแบบ `A001` และกติกาการออกหมายเลขคิว |
| F-009 | ละเมิด Constraint | [config.py:6](/workspaces/660710754-swreqspec/backend/app/config.py:6) | CON-TECH-01 | ค่าเริ่มต้นของ runtime เป็น SQLite ไม่ใช่ PostgreSQL ตามมาตรฐานฐานข้อมูลของระบบจริง | ไม่ใช่ปัญหา: SQLite ใช้เป็นค่าเริ่มต้นสำหรับ dev/test ส่วนระบบจริงสามารถกำหนด PostgreSQL ผ่าน `DATABASE_URL` |
| F-010 | โค้ดไม่มี FR | [frontend/src/App.jsx:4](/workspaces/660710754-swreqspec/frontend/src/App.jsx:4) | FR-BKG-01, FR-BKG-03, FR-BKG-04, FR-BKG-05, FR-BKG-06 | หน้าจอจริงทั้งหมดตาม tasks ยังไม่มี มีเพียงหน้าโครง | ไม่ใช่ปัญหา: Frontend ยังเป็นงานที่ยังไม่ถึงตาม tasks จึงยังไม่มีหน้าจอ booking |
| F-011 | โค้ดไม่มี NFR | ทั้งระบบ | NFR-SEC-01, NFR-USE-01 | ไม่พบ TLS 1.2+ ในการรับส่ง และไม่มีการทดสอบผู้ใช้ใหม่ 8/10 ภายใน 3 นาที | ไม่ใช่ปัญหา: TLS อาจกำหนดที่ infrastructure/proxy และ usability test ไม่สามารถสรุปจาก source code เพียงอย่างเดียว |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| F-008 | ลบ `DELETE /bookings/{booking_id}` จาก `booking/router.py` และลบ `cancel_booking` จาก `booking/service.py` | ไม่พบ endpoint หรือฟังก์ชันยกเลิกคิวในโค้ดแล้ว และการยกเลิก/เลื่อนคิวยังคงอยู่นอก scope ตาม spec |
| F-001 | เปลี่ยน `DAYS_AHEAD` จาก 14 เป็น 30 ใน `backend/app/slots/service.py` | ค่าในโค้ดตรงกับช่วง 30 วันของ FR-BKG-01 แล้ว; ยังเหลือข้อค้นพบ F-002 เรื่อง test ไม่ตรวจขอบเขตวันที่ |
