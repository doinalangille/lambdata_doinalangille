"""
utility functions for working with DataFrames
"""
import datetime as dt
import pandas as pd
from sklearn.model_selection import train_test_split


class Dataframe(object):
    def __init__(self, data):
        """
        Initialize method for working with utils

        Parameters
        ----------
      data: ndarray (structured or homogeneous),
             Iterable, dict, or DataFrame
          Dict can contain Series, arr

        Example
        -------
        my_data = Dataframe(data)
        """
        self.data = data

    def train_val_test(self):
        """
        Train/validate/test split method for a dataframe.
        Uses the train_test_split method from sklearn.model_selection.
        Test size=0.20

        Returns
        -------
        List
          List containing three dataframes

        Examples
        --------
          train = my_data.train_val_test()[0]
          validate = my_data.train_val_test()[1]
          test = my_data.train_val_test()[2]
        """
        train, test = train_test_split(
          self.data, train_size=0.80, test_size=0.20, random_state=42)
        train, val = train_test_split(
          train, train_size=0.80, test_size=0.20, random_state=42)
        return train, val, test


class Dates(Dataframe):
    def __init__(self, data, column):
        """
        Initialize method for the class

        Parameters
        ----------
        data: ndarray (structured or homogeneous),
              Iterable, dict, or DataFrame
          Dict can contain Series, arrays, constants, or list-like objects.
        column : Index or array-like
            Column containing the dates to split

        Example
        -------
        my_df = Dates(df, 'date_recorded')
        """
        super().__init__(data)
        self.column = column

    def date_split(self):
        """
        Split a date column into multiple columns (year, month, day).

        Returns
        -------
        DataFrame
          The dataframe with three more columns added (year, month, day)

        Example
        -------
        my_df.date_split()
        """

        # Convert the date column to datetime format
        self.data[self.column] = pd.to_datetime(self.data[self.column], infer_datetime_format=True)
        # Extract components from date
        self.data['year'] = self.data[self.column].dt.year
        self.data['month'] = self.data[self.column].dt.month
        self.data['day'] = self.data[self.column].dt.day
        return self.data