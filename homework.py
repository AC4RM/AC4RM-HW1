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


regex_pattern = ' '


def play_round():
    """
    Roll a 100 sided die.
    If you draw a value from 1 to 50, you win.
    If you draw a value from 51 to 100, you lose.
    Return True if you win and False if you lose.
    """
