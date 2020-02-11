"""
utility functions for working with DataFrames
"""

import pandas as pd
from sklearn.model_selection import train_test_split

# Function to split dates ("MM/DD/YYYY", etc.) into multiple columns
def date_split(X, col):
    """
    Split a date into the year, month, and day columns.
    X - dataframe;
    col - string, column of X dataframe, containing dates; (example: 'Date_recorded')
    """

    # Convert the date column to datetime format
    X[col] = pd.to_datetime(X[col], infer_datetime_format=True)

    # Extract components from date
    X['year'] = X[col].dt.year
    X['month'] = X[col].dt.month
    X['day'] = X[col].dt.day

    return X

# Train/validate/test split function for a dataframe
def train_val_test(df):
  """
  Train/validate/test split function for a dataframe.
  This function uses the train_test_split method from sklearn.model_selection
  Test size=0.20

  Usage:
  train = train_val_test(df)[0]
  validate = train_val_test(df)[1]
  test = train_val_test(df)[2]
  """
  train, test = train_test_split(df, train_size=0.80, test_size=0.20, random_state=42)
  train, val = train_test_split(train, train_size=0.80, test_size=0.20, random_state=42)
  return train, val, test