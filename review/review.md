- I can easily follow the code layout
  - short, simple functions were easy to understand
  - the longer function had comments for each set of things it was doing
  - no issues with PEP8 styling
- I can easily understand what the code is doing
  - there is good reason for the functions
  - i see that they provide a useful 'shortcut' to common tasks
- I was able to import it into a notebook and use the classes and functions
  - the docstrings were excellent and provided eany easy guide to using the functions
    - colab popped up the docstrings as i was typing. very helpful and nicely formatted

- somewhere, possibly in df_utils.py or the repository readme, include instructions for installing the module
- the docstring for the constructor for the Dates class makes it seem like the 'column' parameter
could be a list
  - passing a list as the column paramerter causes an error in the date_split() method
- the date_split() method in the Dates class changes the underlying dataframe
  - it acts like inplace=True in other dataframe methods
  - should return an altered copy or mention that in the docstring
