import pytest

from app.services import db


def test_index_empty_db(empty_db):
    """Test get_next_index on empty db"""
    assert db.get_next_index() == 0


def test_index_db(db_with_entry):
    """Test get_next_index on non-empty db"""
    assert db.get_next_index() == 1


def test_index_after_insertion(db_with_entry):
    """Test get_next_index after insertion"""
    next_index = db.get_next_index()
    db.add_link(next_index, "https://cloud.florian-dahlitz.de")

    assert db.get_next_index() == 2


def test_get_link(db_with_entry):
    """Get Link"""
    assert db.get_link("0") == "https://florian-dahlitz.de"
