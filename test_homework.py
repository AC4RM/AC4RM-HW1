from homework import *
from pytest import approx
from pathlib import Path
import pandas as pd
import sqlite3
import sklearn
import re


def test_python():
    assert convert_string('Columbia') == 'AIBMULOC'
    assert convert_string('zzzAAA') == 'AAAZZZ'


def test_sql():
    create_table()
    con = sqlite3.connect('homework.db')
    result_df = pd.read_sql_query("SELECT * FROM enrollment;", con)

    schema = list(result_df.columns)
    assert schema == ['id', 'first_name', 'last_name', 'email']
    assert result_df.shape[0] >= 5

    Path('homework.db').unlink(missing_ok=True)


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
