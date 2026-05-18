import pandas as pd
import sqlite3
import streamlit as st
st.title("Sales Dashboard")
conn=sqlite3.connect("sales.db")
df=pd.read_sql("select * from sales",conn)
st.write("data preview")
st.dataframe(df.head())
st.metric("Total Revenue",f"${df['Sales'].sum():,.2f}")
st.metric("Average Rating",f"{df['Rating'].mean():.2f}")
city_sales=df.groupby("City")["Sales"].sum().reset_index()
st.bar_chart(city_sales)
conn.close()