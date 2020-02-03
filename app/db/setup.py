from pathlib import Path

from data.db_session import global_init


def setup_db():
    db_file = str(Path(__file__).parent / "shortener.sqlite")
    global_init(db_file)
