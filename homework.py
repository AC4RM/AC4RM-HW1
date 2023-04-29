import sqlite3
import pandas as pd
import numpy as np


def convert_string(input_string):
    """
    :param input_string: str object
    :return: input_string in upper case and reverse order
    """
    pass


def create_table():
    """
    Create sqlite database file called `homework.db` and a table called `enrollment` with the following columns
    `uni`, `first_name`, `last_name` and `email`. Insert at least 5 rows to the table.
    """
    pass


def train_model():
    np.random.seed(42)
    accidents = pd.read_csv('https://raw.githubusercontent.com/AC4RM/AC4RM-dataset/main/homework/fars2007.csv',
                            index_col=0)
    
