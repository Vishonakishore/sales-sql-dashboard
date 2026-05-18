import pandas as pd
import sqlite3

df = pd.read_csv("data/SuperMarket Analysis.csv")

conn = sqlite3.connect("sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data loaded into SQLite")

conn.close()