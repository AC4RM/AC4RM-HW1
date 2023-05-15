from homework import *
from pytest import approx
import sqlite3
import sklearn
import re


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


def test_model():
    model, score = train_model()
    assert isinstance(model, sklearn.linear_model._base.LinearRegression)
    assert score == approx(0.87, 0.01)


def test_regex():
    assert re.search(regex_pattern, 'abcd\t')
    assert re.search(regex_pattern, '\nabcd')
    assert not re.search(regex_pattern, 'abcd')


def test_monte_carlo():
    result = []
    np.random.seed(42)
    for _ in range(1000):
        result.append(1 if play_round() else 0)

    assert sum(result) == 497
