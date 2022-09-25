# database.py

# built-in imports
import sqlite3
import os
from pathlib import Path

from rich.traceback import install

install(show_locals=True)

HOME_DIR = Path(os.environ["HOME"])
DB_DOCS_PATH: Path = HOME_DIR.joinpath("Documents")

DB_FILE = "habits.db"
DB_FILE_PATH: Path | None = None
if DB_DOCS_PATH.is_dir:
    DB_FILE_PATH = DB_DOCS_PATH.joinpath(DB_FILE)
else:
    os.chdir(HOME_DIR)
    os.mkdir("Documents")


def get_cursor() -> sqlite3.Cursor:

    if not DB_FILE_PATH.exists():
        Path(DB_FILE_PATH).touch()
    with sqlite3.connect(DB_FILE_PATH) as conn:
        cur = conn.cursor()

    return cur


def run_query(sql: str, params: tuple | None = None, db: Path = DB_FILE_PATH) -> list:

    cur = get_cursor()
    try:
        if params:
            cur.execute(sql, params)
        else:
            cur.execute(sql)
    except sqlite3.OperationalError as e:
        return f"{e}\nBad SQL query: {sql}"

    data = cur.fetchall()
    return data


if __name__ == "__main__":
    data = run_query("Gibberish")
