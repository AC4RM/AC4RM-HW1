from homework import *
import sqlite3


def test_python():
    assert convert_string('Columbia') == 'AIBMULOC'
    assert convert_string('zzzAAA') == 'AAAZZZ'


def test_sql():
    create_table()
    con = sqlite3.connect('homework.db')
    cur = con.cursor()
    results = cur.execute(''' SELECT * FROM enrollment;''').fetchall()

    schema = [description[0] for description in cur.description]
    assert schema == ['id', 'first_name', 'last_name', 'email']
    assert len(results) >= 5

