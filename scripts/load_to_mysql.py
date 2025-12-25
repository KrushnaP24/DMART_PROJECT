import os
import pandas as pd
from .mysql_connector import get_connection

BASE_DIR = os.path.dirname(__file__)
DATA_CLEAN_DIR = os.path.join(BASE_DIR, "data_clean")


def read_csv(file_name):
    path = os.path.join(DATA_CLEAN_DIR, file_name)
    print("Reading:", path)
    df = pd.read_csv(path)
    print(f"{file_name} loaded | rows: {len(df)}")
    return df


def truncate_table(table_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SET FOREIGN_KEY_CHECKS=0;")  # disable FK temporarily
    cursor.execute(f"TRUNCATE TABLE {table_name};")
    cursor.execute(f"SET FOREIGN_KEY_CHECKS=1;")
    conn.commit()
    cursor.close()
    conn.close()
    print(f"{table_name} truncated")


def insert_dataframe(df, table_name):
    if df.empty:
        print(f"No rows to insert into {table_name}")
        return
    conn = get_connection()
    cursor = conn.cursor()
    cols = ",".join(df.columns)
    placeholders = ",".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    data = [tuple(row) for row in df.values]
    cursor.executemany(sql, data)
    conn.commit()
    print(f"Inserted {cursor.rowcount} rows into {table_name}")
    cursor.close()
    conn.close()


if __name__ == "__main__":
    print("🚀 Starting data load process...")

    # ---------- TRUNCATE TABLES IN FK-SAFE ORDER ----------
    truncate_table("order_items")
    truncate_table("orders")
    truncate_table("customers")
    truncate_table("products")
    truncate_table("stores")

    # ---------- CUSTOMERS ----------
    customers_df = read_csv("customers.csv")
    customers_df = customers_df.rename(columns={"customer_name": "name"})
    if "state" not in customers_df.columns:
        customers_df["state"] = "Unknown"
    customers_df = customers_df[["customer_id", "name", "city", "state"]]
    insert_dataframe(customers_df, "customers")

    # ---------- PRODUCTS ----------
    products_df = read_csv("products.csv")
    products_df = products_df[["product_id", "name", "category", "unit_price"]]
    insert_dataframe(products_df, "products")

    # ---------- STORES ----------
    stores_df = read_csv("stores.csv")
    stores_df = stores_df.rename(columns={"store_name": "name"})
    stores_df = stores_df[["store_id", "name", "city", "state"]]
    insert_dataframe(stores_df, "stores")

    # ---------- ORDERS ----------
    orders_df = read_csv("orders.csv")
    # Keep only valid customer_id & store_id
    orders_df = orders_df[orders_df["customer_id"].isin(customers_df["customer_id"])]
    orders_df = orders_df[orders_df["store_id"].isin(stores_df["store_id"])]
    orders_df = orders_df[["order_id", "customer_id", "store_id", "order_date", "payment_method"]]
    insert_dataframe(orders_df, "orders")

    # ---------- ORDER ITEMS ----------
    order_items_df = read_csv("order_items.csv")
    order_items_df = order_items_df.rename(columns={"final_prize": "final_price"})
    # Keep only valid order_id & product_id
    order_items_df = order_items_df[order_items_df["order_id"].isin(orders_df["order_id"])]
    order_items_df = order_items_df[order_items_df["product_id"].isin(products_df["product_id"])]
    order_items_df = order_items_df[["order_item_id", "order_id", "product_id", "quantity",
                                     "unit_price", "discount", "final_price"]]
    insert_dataframe(order_items_df, "order_items")

    print("✅ Data load completed successfully")
