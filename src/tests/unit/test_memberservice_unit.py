import pytest
from event.memberservice import MemberService


@pytest.mark.unit
def test_add_member():
    service = MemberService()

    result = service.add_member("Maja")

    assert "Maja" in service.members
    assert result == "Maja added"


@pytest.mark.spy
def test_add_member_spy():
    service = MemberService()

    # simulate weird state
    service.members = None

    try:
        service.add_member("Maja")
        assert False, "Should have failed"
    except Exception:
        assert True