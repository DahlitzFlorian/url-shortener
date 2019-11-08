from pathlib import Path


def _read_db(db_path: Path):
    """Read all links from db text file"""
    links = {}
    with open(str(db_path)) as f:
        for line in f.readlines():
            index, link = line.strip().split(" ")
            links[index] = link
    return links


def get_next_index(db_path: Path):
    """Return the next index used for link generation"""
    links = _read_db(db_path)
    return len(links.keys())


def add_link(db_path: Path, key: str, value: str):
    """Add new key value pair to db"""
    if not (value.startswith("https://") or value.startswith("http://")):
        value = f"https://{value}"

    with open(str(db_path), "a") as f:
        f.write(f"{key} {value}\n")


def get_link(db_path: Path, key: str):
    """Get link for a provided key"""
    links = _read_db(db_path)
    return links.get(key, None)
