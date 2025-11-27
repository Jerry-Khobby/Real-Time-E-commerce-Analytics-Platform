from sqlalchemy import create_engine, text
import pandas as pd

# Database connection
DB_URL = "postgresql://dataeng:dataeng123@localhost:5432/ecommerce"
engine = create_engine(DB_URL)

print("📦 Loading data to PostgreSQL...")

# Create tables
with engine.connect() as conn:
    # Create schema
    conn.execute(text("""
        CREATE SCHEMA IF NOT EXISTS raw;
    """))
    
    # Customers table
    conn.execute(text("""
        DROP TABLE IF EXISTS raw.customers CASCADE;
        CREATE TABLE raw.customers (
            customer_id INTEGER PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            country VARCHAR(100),
            signup_date DATE
        );
    """))
    
    # Products table
    conn.execute(text("""
        DROP TABLE IF EXISTS raw.products CASCADE;
        CREATE TABLE raw.products (
            product_id INTEGER PRIMARY KEY,
            product_name VARCHAR(255),
            category VARCHAR(50),
            price DECIMAL(10,2)
        );
    """))
    
    # Orders table
    conn.execute(text("""
        DROP TABLE IF EXISTS raw.orders CASCADE;
        CREATE TABLE raw.orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER REFERENCES raw.customers(customer_id),
            product_id INTEGER REFERENCES raw.products(product_id),
            quantity INTEGER,
            order_date DATE,
            status VARCHAR(50)
        );
    """))
    
    conn.commit()
    print("✅ Tables created")

# Load CSVs
customers_df = pd.read_csv('./customers.csv')
products_df = pd.read_csv('./products.csv')
orders_df = pd.read_csv('./orders.csv')

customers_df.to_sql('customers', engine, schema='raw', if_exists='append', index=False)
products_df.to_sql('products', engine, schema='raw', if_exists='append', index=False)
orders_df.to_sql('orders', engine, schema='raw', if_exists='append', index=False)

print("✅ Data loaded successfully!")

# Verify
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM raw.orders"))
    count = result.scalar()
    print(f"📊 Total orders in database: {count}")