import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)

# Generate 1000 customers
def generate_customers(n=1000):
    customers = []
    for i in range(1, n+1):
        customers.append({
            'customer_id': i,
            'name': fake.name(),
            'email': fake.email(),
            'country': fake.country(),
            'signup_date': fake.date_between(start_date='-2y', end_date='today')
        })
    return pd.DataFrame(customers)

# Generate 50 products
def generate_products(n=50):
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    products = []
    for i in range(1, n+1):
        products.append({
            'product_id': i,
            'product_name': fake.catch_phrase(),
            'category': random.choice(categories),
            'price': round(random.uniform(10, 500), 2)
        })
    return pd.DataFrame(products)

# Generate 5000 orders (last 90 days)
def generate_orders(n=5000, customer_ids=range(1,1001), product_ids=range(1,51)):
    orders = []
    start_date = datetime.now() - timedelta(days=90)
    
    for i in range(1, n+1):
        order_date = start_date + timedelta(days=random.randint(0, 90))
        orders.append({
            'order_id': i,
            'customer_id': random.choice(list(customer_ids)),
            'product_id': random.choice(list(product_ids)),
            'quantity': random.randint(1, 5),
            'order_date': order_date.date(),
            'status': random.choice(['completed', 'pending', 'cancelled'])
        })
    return pd.DataFrame(orders)

# Generate all data
print("Generating data...")
customers_df = generate_customers(1000)
products_df = generate_products(50)
orders_df = generate_orders(5000)

# Save to CSV (backup)
customers_df.to_csv('customers.csv', index=False)
products_df.to_csv('products.csv', index=False)
orders_df.to_csv('orders.csv', index=False)

print(f"✅ Generated {len(customers_df)} customers")
print(f"✅ Generated {len(products_df)} products")
print(f"✅ Generated {len(orders_df)} orders")