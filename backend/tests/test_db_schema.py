from sqlalchemy import inspect

from app.db.models import AuditLog, Base, Booking, Slot
from app.db.session import engine, init_db


init_db()


def test_schema_contains_booking_tables_and_protected_fields():
    inspector = inspect(engine)
    tables = set(inspector.get_table_names())

    assert {"slots", "bookings", "audit_logs"}.issubset(tables)

    slot_columns = {column["name"] for column in inspector.get_columns("slots")}
    booking_columns = {column["name"] for column in inspector.get_columns("bookings")}
    audit_columns = {column["name"] for column in inspector.get_columns("audit_logs")}

    assert {"slot_date", "start_time", "package_code", "capacity", "remaining"}.issubset(slot_columns)
    assert {"hn", "slot_id", "booking_date", "queue_no", "status", "created_at"}.issubset(booking_columns)
    assert {"actor_id", "action", "hn", "accessed_at"}.issubset(audit_columns)
    assert "national_id" not in booking_columns

    assert Base.metadata.tables["slots"].columns["remaining"].nullable is False
    assert Base.metadata.tables["bookings"].columns["hn"].nullable is False
    assert Base.metadata.tables["audit_logs"].columns["actor_id"].nullable is True

    assert Slot.__tablename__ == "slots"
    assert Booking.__tablename__ == "bookings"
    assert AuditLog.__tablename__ == "audit_logs"
