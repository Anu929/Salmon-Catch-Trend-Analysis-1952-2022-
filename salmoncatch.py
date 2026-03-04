import numpy as np
import pandas as pd
# load data
df = pd.read_csv("D:\Python\SalmonandSeaTroutNets1952-2022.csv")
#view data
print(df.head())
print(df.info())
# check for missing values
df = df.dropna(how="all")
# fill missing values with 0
df = df.fillna(0)
print(df.isnull().sum())
total_catch = df.select_dtypes(include=np.number).sum().sum()
print("Total Catch:", total_catch)
df["Year_Total"] = df.select_dtypes(include=np.number).sum(axis=1)
average_catch = np.mean(df["Year_Total"])
print("Average Yearly Catch:", average_catch)
max_year = df.loc[df["Year_Total"].idxmax()]
min_year = df.loc[df["Year_Total"].idxmin()]
print("Highest Catch Year:\n", max_year)
print("Lowest Catch Year:\n", min_year)
first_20_avg = np.mean(df["Year_Total"][:20])
last_20_avg = np.mean(df["Year_Total"][-20:])
print("\n----- TREND COMPARISON -----")
print("First 20 Years Average:", first_20_avg)
print("Last 20 Years Average:", last_20_avg)
above_avg_years = df[df["Year_Total"] > average_catch]
print("\nNumber of Years Above Average:", len(above_avg_years))
print(above_avg_years[["Year", "Year_Total"]])
max_value = np.max(df["Year_Total"])
latest_value = df["Year_Total"].iloc[-1]
percent_decline = ((max_value - latest_value) / max_value) * 100
print("\n----- PERFORMANCE ANALYSIS -----")
print("Highest Catch:", max_value)
print("Latest Year Catch:", latest_value)
print("Percentage Decline from Peak to Latest Year:", percent_decline, "%")
top5 = df.sort_values("Year_Total", ascending=False).head(5)
print("\n----- TOP 5 HIGHEST CATCH YEARS -----")
print(top5[["Year", "Year_Total"]])