import unittest
import pandas as pd
import sklearn
from lambdata_doinalangille.df_utils import Dates

class DfUtilsTest(unittest.TestCase):
    def test_date_split(self):
        # Add a dataframe
        my_df = Dates({"date": ["01/12/2019", "12/30/2018", "04/23/2019"]}, 'date')
        
        # Test that the function added the proper columns
        result = my_df.date_split()
        cols = result.columns.tolist()
        self.assertIn("year", cols)
        self.assertIn("month", cols)
        self.assertIn("day", cols)

if __name__ == '__main__':
    unittest.main()
