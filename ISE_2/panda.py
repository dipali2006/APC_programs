import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Department": ["CSE", "NTC", "AIML"],
    "Salary": [25000, 75000, 10000]
}

df = pd.DataFrame(data)

print("Employee Data")
print(df)

print("\nHighest Salary Employee Department-wise")
print(df.loc[df.groupby("Department")["Salary"].idxmax()])

print("\nAverage Salary Department-wise")
print(df.groupby("Department")["Salary"].mean())

df["S_Rank"] = df["Salary"].rank(method="dense", ascending=False)

print("\nEmployee Salary Ranking")
print(df.sort_values("Salary_Rank"))
