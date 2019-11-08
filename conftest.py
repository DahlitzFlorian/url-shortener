from pathlib import Path

import pytest


@pytest.fixture
def empty_db(tmpdir):
    db_path = Path(tmpdir) / "db.txt"
    with open(db_path, "w") as f:
        pass
    return tmpdir


@pytest.fixture
def db_with_entry(tmpdir):
    db_path = Path(tmpdir) / "db.txt"
    with open(db_path, "w") as f:
        f.write("0 https://florian-dahlitz.de\n")
    return tmpdir
