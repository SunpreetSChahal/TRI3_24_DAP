# %%
import pandas as pd
from faker import Faker
import random
from datetime import date

# %%
# Initialize Faker
fake = Faker()

# %%
customer_count = 1000
order_count = 5000

# Generate customer data
customer_data = {
    "customer_id": [fake.uuid4() for _ in range(customer_count)],
    "name": [fake.name() for _ in range(customer_count)],
    "email": [fake.email() for _ in range(customer_count)],
    "phone_number": [fake.phone_number() for _ in range(customer_count)]
}

customers_df = pd.DataFrame(customer_data)

# Generate purchase order data
product_ids = [f'product_{i}' for i in range(1, 101)]
purchase_data = {
    "order_id": [fake.uuid4() for _ in range(order_count)],
    "customer_id": [random.choice(customer_data["customer_id"]) for _ in range(order_count)],
    "product_id": [random.choice(product_ids) for _ in range(order_count)],
    "quantity": [random.randint(1, 10) for _ in range(order_count)],
    "cost": [round(random.uniform(10.0, 500.0), 2) for _ in range(order_count)],
    "order_date": [date.today()]
}
purchase_orders_df = pd.DataFrame(purchase_data)

# %%
display(purchase_orders_df.head(), customers_df.head())

# %%
customers_df.to_csv(f'results/customer_information.csv')
purchase_orders_df.to_csv(f'results/purchase_orders.csv')

# %%



