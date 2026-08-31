import pandas as pd

df = pd.DataFrame({
    "store": ["north", "south", "north", "south", "north"],
    "sales": [120, 150, 90, 130, 110]
})

# [[{store: north, sales: 120},  {north, 90}, {north, 110}], [{south, 150}, {south, 130}]]
df.groupby("store")


# [[{sales: 120},  { 90}, {110}], [{ 150}, {130}]]
df.groupby("store")["sales"]

# [120 + 90 + 110, 150 + 130]
print(df.groupby("store")["sales"].sum())

print(df.groupby("store")["sales"].mean())

print(df.groupby("store")["sales"].max())