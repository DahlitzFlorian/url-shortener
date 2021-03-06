from data import db_session
from data.link import Link
from services.shortener import saturate
from sqlalchemy.orm import Session


def get_next_index():
    """Return the next index used for link generation"""
    session: Session = db_session.create_session()
    result = session.execute("SELECT MAX(ROWID) FROM links")

    for row in result:
        try:
            return row[0] + 1
        except TypeError:
            return 1


def add_link(key: str, value: str):
    """Add new key value pair to db"""
    if not (value.startswith("https://") or value.startswith("http://")):
        value = f"https://{value}"

    session: Session = db_session.create_session()
    link = Link(short_link=key, destination=value)
    session.add(link)
    session.commit()


def get_link(key: str):
    """Get link for a provided key"""
    actual_id = saturate(key.rsplit("/", 1)[-1])
    session: Session = db_session.create_session()
    try:
        return session.query(Link).get({"id": actual_id}).destination
    except AttributeError:
        return None


def check_link_exist(destination: str):
    """Check if link already exists and return otherwise return None"""
    session: Session = db_session.create_session()
    result = session.execute(
        f"SELECT short_link FROM links WHERE destination = '{destination}'",
    )  # fix possible SQL injection

    for row in result:
        return row[0]
    else:
        return None
