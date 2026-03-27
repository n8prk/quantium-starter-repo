import pandas as pd
from pathlib import Path

def load_data(filepath):
    return pd.read_csv(filepath)

df_one = load_data(Path("data/daily_sales_data_0.csv"))
df_two = load_data(Path("data/daily_sales_data_1.csv"))
df_three = load_data(Path("data/daily_sales_data_2.csv"))

df = pd.concat([df_one, df_two, df_three], ignore_index=True)
df.to_csv("data/output.csv", index=False)