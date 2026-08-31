import pandas as pd

df = pd.DataFrame({
    "product": ["pen", "notebook", "eraser", "marker", "folder", "tape"],
    "category": ["A", "B", "A", "A", "B", "A"],
    "price": [1.5, 3.2, 0.8, 2.7, 2.1, 1.9],
    "stock": [120, 45, 200, 35, 60, 80]
})

print(df[(df["category"] == "A") & (df["price"] > 1)].sort_values("stock", ascending = False)[["product", "price", "stock"]])