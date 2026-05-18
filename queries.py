import sqlite3
import pandas as pd
conn=sqlite3.connect("sales.db")

query="""
select City,SUM(Sales) as revenue
from sales
group by City
order by revenue desc"""
print("Revenue by city")
print(pd.read_sql(query,conn))

query2="""
select "Product line",SUM(Sales) as revenue
from sales
group by "Product line"
order by revenue desc"""
print("\nBest product")
print(pd.read_sql(query,conn))

query3="""
select Payment,count(*) as count
from sales
group by payment
order by count desc"""
print("\nMost used payment method")
print(pd.read_sql(query,conn))

query4="""
select branch,city,avg(rating) as avg_rating
from sales
group by branch,city
order by avg_rating desc"""
print("\nBest branch")
print(pd.read_sql(query4,conn))
conn.close()