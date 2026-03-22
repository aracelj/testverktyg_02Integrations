import pytest
from event.app import process_item, DATABASE


@pytest.fixture(autouse=True)
def clear_db():
    DATABASE.clear()


@pytest.mark.integration
def test_process_item_success():
    result = process_item({"name": "apple"})

    assert result == "ok"
    assert len(DATABASE) == 1
    assert DATABASE[0]["name"] == "apple"


@pytest.mark.integration
def test_process_item_empty():
    with pytest.raises(ValueError):
        process_item({})

    # nothing saved if it fails
    assert len(DATABASE) == 0


@pytest.mark.spy
def test_database_crash():
    DATABASE.clear()  # or DATABASE = []

    result = process_item({"name": "banana"})

    assert result == "ok"