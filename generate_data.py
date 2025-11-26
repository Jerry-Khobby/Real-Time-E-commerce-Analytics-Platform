import pandas as pd 
from faker import Faker 
import random 
from datetime import datetime, timedelta



fake = Faker()
Faker.seed(42)

""" 
I want to generate synthetic data for testing a customer database. The data should include the following fields for each customer:
- Customer ID: A unique identifier for each customer. 

"""

def generate_customers(n=1000):
  customers = []
  for i in range(1, n+1):
    customer ={
      "Customer ID": i,
      "First Name": fake.first_name(),
      "Last Name": fake.last_name(),
      "Email": fake.email(),
      "country": fake.country(),
      "signup_date": fake.date_between(start_date='-2y', end_date='today' )
    }
    customers.append(customer)
    return pd.DataFrame(customers)
  
  

#Generate 5000 orders (last 90 days)

def generate_products(n=50):
  products = []
  for i in range(1, n+1):
    product = {
      "Product ID": i,
      "Product Name": fake.catch_phrase(),
      "Category": random.choice(['Electronics', 'Clothing', 'Home', 'Books', 'Sports']),
      "Price": round(random.uniform(10, 500), 2)
    }
    products.append(product)
  return pd.DataFrame(products)







#Generate 5000 orders (last 90 days)
def generate_orders(n=5000,customer_ids=range(1,1001),product_ids=range(1,51)):
  orders=[]
  start_date= datetime.now()-timedelta(days=90)
  for i in range(1, n+1):
    order_date = start_date + timedelta(days=random.randint(0, 90))
    order = {
      "Order ID": i,
      "Customer ID": random.choice(customer_ids),
      "Product ID": random.choice(product_ids),
      "Quantity": random.randint(1, 5),
      "Order Date": order_date.date(),
      "status":random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled'])
    }
    orders.append(order)
  return pd.DataFrame(orders)



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