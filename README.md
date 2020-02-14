# lambdata_doinalangille Package
A collection of data science helper functions

## How to install
```python
pip install -i https://test.pypi.org/simple/ lambdata-doinalangille
```

## Examples
```python
my_data = Dataframe(data)
train = my_data.train_val_test()[0]
validate = my_data.train_val_test()[1]
test = my_data.train_val_test()[2]

my_df = Dates(df, 'date_recorded')
my_df.date_split()
```

