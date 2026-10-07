# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md Draft v3 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 15.45 | test: backend 10 ผ่าน 0 ไม่ผ่าน, frontend 3 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 | T-02 เสร็จ, T-10 เสร็จ รอทีมตรวจ | [slots/service.py:list_available_slots](/workspaces/660710754-swreqspec/backend/app/slots/service.py:11), [slots/router.py:get_slots](/workspaces/660710754-swreqspec/backend/app/slots/router.py:12), [SlotPicker.jsx:SlotPicker](/workspaces/660710754-swreqspec/frontend/src/pages/SlotPicker.jsx:8) | `test_AC_BKG_05` ผ่าน แต่ไม่ตรวจขอบเขต 30 วัน/จำนวนที่นั่ง; หน้าจอไม่มี test ตรวจวันและข้อความตาม UI | ช่องโหว่ |
| FR-BKG-02 | AC-BKG-02 | T-04 เสร็จ รอทีมตรวจ | [booking/service.py:create_booking](/workspaces/660710754-swreqspec/backend/app/booking/service.py:20), [booking/router.py:create_booking](/workspaces/660710754-swreqspec/backend/app/booking/router.py:23) | `test_TC_BKG_02_1_reject_duplicate_day`, `test_TC_BKG_02_2_allow_different_day`, `test_TC_BKG_02_3_create_new_booking` ผ่าน; หมายเลขคิวเดิมยังรอ Q-02 | รอ Q-02 |
| FR-BKG-03 | AC-BKG-03 | T-05 พร้อมทำ, T-11 เสร็จ รอทีมตรวจ, T-12 พร้อมทำ | [ConfirmBooking.jsx:ConfirmBooking](/workspaces/660710754-swreqspec/frontend/src/pages/ConfirmBooking.jsx:4) รองรับผล 409 ในหน้าจอ แต่ยังไม่มี backend เสนอทางเลือก | `AC-BKG-03` ผ่านเฉพาะข้อความและจำนวนปุ่ม; ไม่มี test backend ตรวจ 409/3 ช่วง/ไม่สร้าง booking | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03 เสร็จ, T-06 รอ Q-02 | [booking/service.py:create_booking](/workspaces/660710754-swreqspec/backend/app/booking/service.py:20), [booking/router.py:create_booking](/workspaces/660710754-swreqspec/backend/app/booking/router.py:23) | `test_TC_BKG_01_1_last_seat`, `test_TC_BKG_01_2_no_seat_left` ผ่านสำหรับบันทึก/ตัดที่นั่ง; หมายเลขคิวและการส่งข้อความยังไม่ตรวจ | ช่องโหว่ |
| FR-BKG-05 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีโค้ด notify/คิวส่งซ้ำ | ไม่มี test | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02 เสร็จ, T-10 เสร็จ รอทีมตรวจ | [slots/service.py:list_available_slots](/workspaces/660710754-swreqspec/backend/app/slots/service.py:11), [SlotPicker.jsx:SlotPicker](/workspaces/660710754-swreqspec/frontend/src/pages/SlotPicker.jsx:8) | `SlotPicker.test.jsx` ผ่านและตรวจเปลี่ยน package แล้วโหลดช่วงเวลาใหม่ แต่ไม่มี AC ที่ทีมอนุมัติ และ Q-04 ยังเปิด | รอ Q-04 |
| NFR-PERF-01 | AC-BKG-05 | T-02 เสร็จ | [test_AC_BKG_05.py:test_AC_BKG_05](/workspaces/660710754-swreqspec/backend/tests/test_AC_BKG_05.py:6) | ผ่าน แต่ยิง 200 request แบบเรียงลำดับ ไม่ใช่ผู้ใช้พร้อมกัน 200 คน | ช่องโหว่ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่พบการตั้งค่า TLS 1.2+ ใน source/proxy config | ไม่มี test | ช่องโหว่ |
| NFR-REL-02 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีโค้ดส่งซ้ำ | ไม่มี test | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มี usability test ผู้ใช้ใหม่ 8 ใน 10 ภายใน 3 นาที | ไม่มี test | ช่องโหว่ |
| CON-TECH-01 | ไม่มี AC ตรง ๆ | T-01 เสร็จ | [config.py:DATABASE_URL](/workspaces/660710754-swreqspec/backend/app/config.py:4) รองรับ PostgreSQL ผ่าน env แต่ default เป็น SQLite | `test_T01_tables_created` ผ่านบน SQLite ไม่ยืนยัน PostgreSQL | ช่องโหว่ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 พร้อมทำ | มีตาราง [models.py:AuditLog](/workspaces/660710754-swreqspec/backend/app/db/models.py:38) แต่ไม่มี middleware บันทึกจริง | ไม่มี test | ยังไม่ถึง |
| IF-IDP-01 | AC-BKG-01 | T-03 เสร็จ | [auth/idp.py:get_verified_hn](/workspaces/660710754-swreqspec/backend/app/auth/idp.py:7) ตรวจ Authorization ก่อน POST /bookings | `test_TC_BKG_01_3_not_verified` ผ่าน | ครบ |
| IF-HIS-01 | ไม่มี AC ตรง ๆ | T-01 เสร็จ, T-09 พร้อมทำ | [models.py:Booking](/workspaces/660710754-swreqspec/backend/app/db/models.py:25) เก็บ HN และไม่มี `national_id` แต่ยังไม่มี HIS client/lookup | `test_T01_no_national_id` ผ่านเฉพาะ schema | ยังไม่ถึง |
| IF-NOT-01 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มี asynchronous notification enqueue | ไม่มี test | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| [slots/router.py:GET /slots](/workspaces/660710754-swreqspec/backend/app/slots/router.py:12) | FR-BKG-01, FR-BKG-06 | บางส่วน | กรองแพ็กเกจและช่วงวันที่/ที่นั่งว่างได้ แต่การแสดงผล UI และเกณฑ์ AC ยังไม่ครบ |
| [slots/service.py:list_available_slots](/workspaces/660710754-swreqspec/backend/app/slots/service.py:11) | FR-BKG-01, FR-BKG-06 | ตรงบางส่วน | ใช้ 30 วันและ `remaining > 0`; ยังไม่มี test ตรวจขอบเขต |
| [booking/router.py:POST /bookings](/workspaces/660710754-swreqspec/backend/app/booking/router.py:23) | FR-BKG-02, FR-BKG-04, IF-IDP-01 | ตรงบางส่วน | กันจองซ้ำและตรวจตัวตนได้ แต่ไม่ส่งข้อความยืนยันและไม่คืนหมายเลขคิวตาม Q-02 |
| [booking/service.py:create_booking](/workspaces/660710754-swreqspec/backend/app/booking/service.py:20) | FR-BKG-02, FR-BKG-04 | ตรงบางส่วน | บันทึก/ตัดที่นั่ง/กันซ้ำได้ แต่ยังไม่มี notification และ `queue_no` ว่างตาม Q-02 |
| [auth/idp.py:get_verified_hn](/workspaces/660710754-swreqspec/backend/app/auth/idp.py:7) | IF-IDP-01 | ตรงในขอบเขต mock | ตรวจ token prefix จำลอง ไม่ใช่การเชื่อม IDP จริง |
| [frontend/src/api/client.js:api](/workspaces/660710754-swreqspec/frontend/src/api/client.js:5) | FR-BKG-01, FR-BKG-03, FR-BKG-04 | ไม่ตรงบางส่วน | มี `cancelBooking` สำหรับ DELETE ซึ่งเป็นการยกเลิกคิวที่อยู่ใน Out of scope |
| [frontend/src/pages/SlotPicker.jsx:SlotPicker](/workspaces/660710754-swreqspec/frontend/src/pages/SlotPicker.jsx:8) | FR-BKG-01, FR-BKG-06, UI-BKG-01 | ไม่ตรงบางส่วน | เปลี่ยนแพ็กเกจได้ แต่ข้อความเป็น “ว่าง N” ไม่ใช่ “เหลือ N ที่” และไม่มีการแสดงช่วงวันตาม UI ที่ต้องตรง |
| [frontend/src/pages/ConfirmBooking.jsx:ConfirmBooking](/workspaces/660710754-swreqspec/frontend/src/pages/ConfirmBooking.jsx:4) | FR-BKG-03, FR-BKG-04, UI-BKG-02 | ตรงบางส่วน | มีข้อความ “ช่วงเวลาเต็ม” และ 3 ตัวเลือก; ไม่พบปุ่มยกเลิกแล้ว แต่ยังไม่มี state แสดงกรณีมีคิวเดิมตาม UI-BKG-02 |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง

ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-002 | test อ่อน | [test_AC_BKG_05.py:test_AC_BKG_05](/workspaces/660710754-swreqspec/backend/tests/test_AC_BKG_05.py:6) | NFR-PERF-01 | วัด 200 request แบบเรียงลำดับ ไม่ใช่ผู้ใช้พร้อมกัน 200 คน จึงยืนยัน NFR ไม่ได้ | แก้โค้ด: ปรับ test ให้จำลองผู้ใช้พร้อมกัน 200 คน |
| F-003 | AC ไม่มี test | [booking/service.py:create_booking](/workspaces/660710754-swreqspec/backend/app/booking/service.py:20) | FR-BKG-04, AC-BKG-01 | ไม่มี assert หมายเลขคิวและไม่มี test การส่งคำขอข้อความ แม้ FR ระบุทั้งสองอย่าง | เพิ่ม Q-xx: ต้องตอบ Q-02 ก่อนเพิ่ม assertion หมายเลขคิว |
| F-004 | โค้ดไม่มี FR | [booking/router.py:POST /bookings](/workspaces/660710754-swreqspec/backend/app/booking/router.py:23) | FR-BKG-04, IF-NOT-01 | การจองไม่ enqueue SMS/LINE แบบ asynchronous | แก้โค้ด |
| F-005 | FR ไม่มี AC | [spec.md](/workspaces/660710754-swreqspec/specs/001-booking/spec.md) | FR-BKG-06 | ไม่มี AC ที่ตรวจการเปลี่ยนแพ็กเกจ แม้มี implementation/test บางส่วน | แก้ spec |
| F-009 | ละเมิด Constraint | [config.py:DATABASE_URL](/workspaces/660710754-swreqspec/backend/app/config.py:4) | CON-TECH-01 | default runtime เป็น SQLite ไม่ใช่ PostgreSQL | ไม่ใช่ปัญหา: SQLite ใช้เฉพาะ dev/test และระบบจริงตั้ง `DATABASE_URL` ได้ |
| F-010 | โค้ดไม่มี FR | [frontend/src/App.jsx:App](/workspaces/660710754-swreqspec/frontend/src/App.jsx:4) | FR-BKG-01 ถึง FR-BKG-06 | frontend มี SlotPicker/ConfirmBooking บางส่วนแล้ว แต่ยังขาด BookingResult, backend FR-BKG-03/05 และการต่อ flow จริงครบถ้วน | ไม่ใช่ปัญหา: ส่วนที่เหลือยังเป็น task ที่ยังไม่ถึง |
| F-011 | โค้ดไม่มี NFR | ทั้งระบบ | NFR-SEC-01, NFR-USE-01 | ไม่พบ TLS 1.2+ ใน source และไม่มี usability test 8/10 | ไม่ใช่ปัญหา: TLS อยู่ที่ infrastructure/proxy และ usability ต้องทดสอบกับผู้ใช้จริง |
| F-012 | โค้ดอยู่ใน Out of scope | [frontend/src/api/client.js:cancelBooking](/workspaces/660710754-swreqspec/frontend/src/api/client.js:17) | Out of scope UC-02 | ยังมี client method สำหรับ DELETE `/bookings/{booking_id}` แม้การยกเลิก/เลื่อนคิวอยู่นอก scope และ endpoint backend ถูกลบแล้ว | |
| F-013 | ไม่ตรง mockup | [frontend/src/pages/SlotPicker.jsx:SlotPicker](/workspaces/660710754-swreqspec/frontend/src/pages/SlotPicker.jsx:8) | UI-BKG-01, FR-BKG-01 | UI ใช้ข้อความ “ว่าง N” แทน “เหลือ N ที่” และไม่แสดงชุดวัน/วันที่ภายใน 30 วันตามส่วนที่ spec ระบุว่าต้องตรง | |
| F-014 | mockup เกิน spec | [mockups/UI-BKG-01-select-slot.html](/workspaces/660710754-swreqspec/specs/001-booking/mockups/UI-BKG-01-select-slot.html:77) | ไม่มี FR/NFR/CON รองรับ | Mockup มีตัวเลือก “แจ้งเตือนก่อนวันตรวจ 1 วัน” แต่ spec ไม่ได้กำหนด requirement เรื่องนี้ จึงยังไม่ถือเป็น requirement ที่ขาด และควรถามทีมตาม Q-05 ว่าต้องการเพิ่มเป็น requirement หรือไม่ | เพิ่ม Q-05 |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| F-008 | ลบ `DELETE /bookings/{booking_id}` และ `cancel_booking` จาก backend | ไม่พบ endpoint/function ยกเลิกคิวใน backend และการยกเลิก/เลื่อนคิวยังคงอยู่นอก scope |
| F-001 | เปลี่ยน `DAYS_AHEAD` จาก 14 เป็น 30 | ค่าในโค้ดตรงกับ FR-BKG-01 แล้ว |
| F-006 | ลบ `national_id` จาก request model, ใช้ `extra="forbid"` และไม่เขียนลง log | request ไม่รับ field นี้ และ booking log ใช้เฉพาะ slot/HN |
| F-007 | ลบการสร้างเลขคิวแบบ `A001` และใช้ `queue_no=None` พร้อม comment รอ Q-02 | ไม่พบการ hardcode/คำนวณเลขคิวใน production code |
