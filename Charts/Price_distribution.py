import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "all_books.csv"

df = pd.read_csv(csv_path)

df["Price"] = (
    df["Price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

plt.hist(df["Price"], bins=10)

plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Number of Books")

plt.show()