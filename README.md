### Introduction
- This the week 1 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Complete the `convert_string` function in `homework.py` that converts the input string into upper case and return it in reverse order. 
   - E.g. `convert_string("aBcD")` => `DCBA`
2. Create sqlite database file called `homework.db` and a table called `enrollment` with the following columns `id`(primary key), `first_name`, `last_name` and `email`. Insert at least 5 rows to the table.
3. In this homework, we will study simple linear regression with the traffic accident data set
   - Among all the columns, we pay attention to 'travspd' (i.e. travel speed) and 'injury' columns
   - Use pandas `pd.cut` function (with labels=False) to bin the `travspd` into 20 bins and introduce a new column of bin numbers
   - Group the dataframe by the `speedBin` column and calculate the mean of `travspd` and `injury`
     - `travspd` will be your X and `injury` will be your y
     - Split the X and y into training and testing set (80/20) and use a random seed of `42`
     - Fit a linear regression model using your training data
     - Return the linear regression model object and your test score