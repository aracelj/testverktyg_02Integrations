import pytest
from event.event import Event


def test_register_new_member_integration():
    event = Event()

    result = event.register_new_member("Alice")

    assert "Alice" in event.members
    assert event.event_log == ["Alice was registered as a new member"]
    assert result == "Alice successfully registered"