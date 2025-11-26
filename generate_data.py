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
      "Product Name": fake.word().title(),
      "Category": random.choice(['Electronics', 'Clothing', 'Home', 'Books', 'Sports']),
      "Price": round(random.uniform(10, 500), 2)
    }
    products.append(product)
  return pd.DataFrame(products)