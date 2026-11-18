import matplotlib.pyplot as plt
import pandas as pd

orders = pd.read_excel("orders.xlsx")

# orders["unit_price"].plot(kind="hist")

# plt.title("Unit price distribution")
# plt.xlabel("unit price")
# plt.ylabel("frequency")
# plt.show()


# orders.groupby("product")["quantity"].sum().plot(kind="bar")

# plt.title("Quantity Sold by Product")
# plt.xlabel("Product")
# plt.ylabel("Total Quantity")
# plt.show()

orders.plot(
    kind="scatter",
    x="unit_price",
    y="quantity"
)

plt.title("Unit Price vs Quantity")
plt.show()

