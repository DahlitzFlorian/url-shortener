def _read_db():
    """Read all links from db text file"""
    links = {}
    with open("db.txt") as f:
        for line in f.readlines():
            index, link = line.strip().split(" ")
            links[index] = link
    return links


def get_next_index():
    """Return the next index used for link generation"""
    links = _read_db()
    return len(links.keys())


def add_link(key: str, value: str):
    """Add new key value pair to db"""
    with open("db.txt", "a") as f:
        f.write(f"{key} {value}")


def get_link(key: str):
    """Get link for a provided key"""
    links = _read_db()
    return links.get(key, None)
