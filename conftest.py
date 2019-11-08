import pytest


@pytest.fixture
def empty_db(tmpdir):
    with open("db.txt", "w") as f:
        pass
    return tmpdir


@pytest.fixture
def db_with_entry(tmpdir):
    with open("db.txt", "w") as f:
        f.write("0 https://florian-dahlitz.de\n")
    return tmpdir
