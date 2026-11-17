#%%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
if not os.path.exists("dataset.csv"):
    rng = np.random.default_rng(42)
    n = 40
    study = rng.uniform(1, 10, n).round(1)
    sleep = rng.uniform(4, 9, n).round(1)
    attend = rng.uniform(55, 100, n).round(0)
    marks = (30 + 4 * study + 0.3 * attend + 1.5 * sleep + rng.normal(0, 4, n)).clip(0, 100).round(0)
    sample = pd.DataFrame({
        "Month": pd.date_range("2026-01-01", periods=n, freq="W").strftime("%d-%b"),
        "Department": rng.choice(["CSE", "ECE", "Mechanical", "Civil"], n),
        "StudyHours": study,
        "SleepHours": sleep,
        "Attendance": attend,
        "Marks": marks,
    })
    sample.to_csv("dataset.csv", index=False)
 
df = pd.read_csv("dataset.csv")
print("First 5 rows:\n", df.head(), "\n")
print("Shape (rows, columns):", df.shape, "\n")
print("Column info:")
df.info()
print("\nStatistical summary:\n", df.describe(), "\n")
print("Missing values per column:\n", df.isnull().sum(), "\n")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(9, 5))
plt.plot(df.index + 1, df["Marks"], marker="o", color="royalblue", label="Marks")
plt.title("Line Plot: Marks Across Records")
plt.xlabel("Record Number")
plt.ylabel("Marks")
plt.legend()
plt.tight_layout()
plt.savefig("line_plot.png", dpi=150)
plt.show()

avg_marks = df.groupby("Department")["Marks"].mean()
plt.figure(figsize=(7, 5))
plt.bar(avg_marks.index, avg_marks.values, color=["#4C72B0", "#55A868", "#C44E52", "#8172B2"])
plt.title("Bar Plot: Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
for i, v in enumerate(avg_marks.values):
    plt.text(i, v + 0.5, f"{v:.1f}", ha="center")   # value labels on bars
plt.tight_layout()
plt.savefig("bar_plot.png", dpi=150)
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(df["StudyHours"], df["Marks"], c="darkorange", edgecolor="black", label="Student")
# optional trend line
m, c = np.polyfit(df["StudyHours"], df["Marks"], 1)
plt.plot(df["StudyHours"], m * df["StudyHours"] + c, color="red", linestyle="--", label="Trend line")
plt.title("Scatter Plot: Study Hours vs Marks")
plt.xlabel("Study Hours per Day")
plt.ylabel("Marks")
plt.legend()
plt.tight_layout()
plt.savefig("scatter_plot.png", dpi=150)
plt.show()
corr = df.select_dtypes(include="number").corr()
print("Correlation matrix:\n", corr.round(2))
 
plt.figure(figsize=(7, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, linewidths=0.5)
plt.title("Heatmap: Correlation Between Numerical Variables")
plt.tight_layout()
plt.savefig("heatmap.png", dpi=150)
plt.show()
 
print("\nAll plots created and saved as PNG files.")
 
# %%
