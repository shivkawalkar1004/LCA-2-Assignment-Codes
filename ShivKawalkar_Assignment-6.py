#%%
import pandas as pd
import numpy as np
data = {
    "Name":  ["Shiv", "Sammit", "Soham", "Chinmay", "Siddhesh", "Sammit", np.nan],
    "Marks": [85, np.nan, 78, 92, 82, 88, 67],
    "City":  ["Pune", "Mumbai", np.nan, "Nashik", "Pune", "Mumbai", "Nagpur"]
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
print("\nAfter dropna():\n", df.dropna())
df_filled = df.copy()
df_filled["Marks"] = df_filled["Marks"].fillna(df_filled["Marks"].mean())
df_filled["City"] = df_filled["City"].fillna("Unknown")
df_filled["Name"] = df_filled["Name"].fillna("Unknown")
print("\nAfter fillna():\n", df_filled)
print("\nDuplicate rows:\n", df_filled.duplicated())
df_clean = df_filled.drop_duplicates()
print("\nAfter drop_duplicates():\n", df_clean)
print("\nName & Marks only:\n", df_clean.loc[:, ["Name", "Marks"]])
print("\nMarks > 80:\n", df_clean.loc[df_clean["Marks"] > 80])
print("\nStudents from Pune:\n", df_clean.loc[df_clean["City"] == "Pune", ["Name", "Marks"]])


# %%
