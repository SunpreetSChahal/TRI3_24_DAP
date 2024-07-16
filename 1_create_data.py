# %%
import pandas as pd
from faker import Faker
import random

# %%
# Initialize Faker
fake = Faker()

# %%
# Generate customer data
customer_data = {
    "customer_id": [fake.uuid4() for _ in range(1000)],
    "name": [fake.name() for _ in range(1000)],
    "email": [fake.email() for _ in range(1000)],
    "phone_number": [fake.phone_number() for _ in range(1000)]
}

customers_df = pd.DataFrame(customer_data)

# Generate purchase order data
product_ids = [f'product_{i}' for i in range(1, 101)]
purchase_data = {
    "order_id": [fake.uuid4() for _ in range(5000)],
    "customer_id": [random.choice(customer_data["customer_id"]) for _ in range(5000)],
    "product_id": [random.choice(product_ids) for _ in range(5000)],
    "quantity": [random.randint(1, 10) for _ in range(5000)],
    "cost": [round(random.uniform(10.0, 500.0), 2) for _ in range(5000)],
    "order_date": [fake.date_this_year() for _ in range(5000)]
}
purchase_orders_df = pd.DataFrame(purchase_data)

# %%
display(purchase_orders_df.head(), customers_df.head())

# %%
customers_df.to_csv(f'results/customer_information.csv')
purchase_orders_df.to_csv(f'results/purchase_orders.csv')

# %%



