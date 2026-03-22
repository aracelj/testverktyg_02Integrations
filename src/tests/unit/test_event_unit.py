from event.event import Event

def test_sign_up_adds_user():
    event = Event()

    event.sign_up("Maja")

    assert "Maja" in event.members
    assert len(event.members) == 1