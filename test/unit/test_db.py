from pathlib import Path

import pytest

from app.services import db


def test_index_empty_db(empty_db):
    """Test get_next_index on empty db"""
    assert db.get_next_index(Path(empty_db) / "db.txt") == 0


def test_index_db(db_with_entry):
    """Test get_next_index on non-empty db"""
    assert db.get_next_index(Path(db_with_entry) / "db.txt") == 1


def test_index_after_insertion(db_with_entry):
    """Test get_next_index after insertion"""
    next_index = db.get_next_index(Path(db_with_entry) / "db.txt")
    db.add_link(Path(db_with_entry) / "db.txt", next_index, "https://cloud.florian-dahlitz.de")

    assert db.get_next_index(Path(db_with_entry) / "db.txt") == 2


def test_get_link(db_with_entry):
    """Get Link"""
    assert db.get_link(Path(db_with_entry) / "db.txt", "0") == "https://florian-dahlitz.de"
