import sqlite3

import pytest

import database


def test_get_cursor():
    cur = database.get_cursor()
    assert isinstance(cur, sqlite3.Cursor) == True


def test_quert_bad_sql_no_params():
    data = database.run_query("gibberish")
    assert type(data) == list
