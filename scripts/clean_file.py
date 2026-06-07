import pandas as pd

df = pd.read_csv("books_details.csv")

print(df.info())
print(df.isnull().sum())
print(df.head())