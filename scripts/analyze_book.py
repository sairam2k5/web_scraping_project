import pandas as pd
import os

print("Current Folder:", os.getcwd())

df = pd.read_csv("all_books.csv")

# Clean Price column
df["Price"] = (
    df["Price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

# Save cleaned data to a new CSV
df.to_csv("all_books_cleaned.csv", index=False)

# Analysis
print("Average Price:", df["Price"].mean())
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())
df.to_csv("all_books_cleaned.csv", index=False)