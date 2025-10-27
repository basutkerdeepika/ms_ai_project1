# -----------------------------------------------
# Analyzing Customer Orders Using Python
# -----------------------------------------------

# 1. Store customer orders
customers = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Each order: (customer_name, product, price, category)
orders = [
    ("Alice", "Laptop", 900, "Electronics"),
    ("Alice", "Headphones", 50, "Electronics"),
    ("Bob", "T-Shirt", 20, "Clothing"),
    ("Bob", "Shoes", 60, "Clothing"),
    ("Charlie", "Blender", 45, "Home Essentials"),
    ("Charlie", "Microwave", 120, "Home Essentials"),
    ("David", "Laptop", 900, "Electronics"),
    ("David", "Shoes", 60, "Clothing"),
    ("Eve", "Lamp", 35, "Home Essentials"),
    ("Eve", "Headphones", 50, "Electronics"),
]

# Dictionary: customer → list of orders
customer_orders = {}
for order in orders:
    name, product, price, category = order
    customer_orders.setdefault(name, []).append((product, price, category))

# 2. Classify products by category
product_to_category = {product: category for _, product, _, category in orders}
unique_categories = set(product_to_category.values())

print("Available Product Categories:", unique_categories)

# 3. Analyze customer orders (classify buyers)
customer_spending = {}
customer_classification = {}

for name, order_list in customer_orders.items():
    total = sum(price for _, price, _ in order_list)
    customer_spending[name] = total
    if total > 100:
        customer_classification[name] = "High-value Buyer"
    elif 50 <= total <= 100:
        customer_classification[name] = "Moderate Buyer"
    else:
        customer_classification[name] = "Low-value Buyer"

# 4. Generate business insights
# Revenue per category
revenue_per_category = {}
for _, product, price, category in orders:
    revenue_per_category[category] = revenue_per_category.get(category, 0) + price

# Unique products
unique_products = {product for _, product, _, _ in orders}

# Customers who purchased Electronics
electronics_customers = [name for name, order_list in customer_orders.items()
                         if any(cat == "Electronics" for _, _, cat in order_list)]

# Top 3 spenders
top_spenders = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)[:3]

# 5. Organize and display data
print("\nCustomer Summary:")
for name in customers:
    print(f"{name} → Total Spending: ${customer_spending[name]} "
          f"({customer_classification[name]})")

print("\nRevenue by Category:", revenue_per_category)
print("Unique Products:", unique_products)
print("Customers who bought Electronics:", electronics_customers)
print("Top 3 Spenders:", top_spenders)

# Customers who purchased from multiple categories
multi_category_customers = [name for name, order_list in customer_orders.items()
                            if len(set(cat for _, _, cat in order_list)) > 1]

print("Customers who purchased from multiple categories:", multi_category_customers)

# Customers who bought both Electronics and Clothing
electronics_buyers = {name for name, order_list in customer_orders.items()
                      if any(cat == "Electronics" for _, _, cat in order_list)}
clothing_buyers = {name for name, order_list in customer_orders.items()
                   if any(cat == "Clothing" for _, _, cat in order_list)}
common_customers = electronics_buyers & clothing_buyers

print("Customers who bought both Electronics and Clothing:", common_customers)
