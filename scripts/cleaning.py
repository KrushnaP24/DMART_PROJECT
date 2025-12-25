import pandas as pd
import os

RAW_PATH = "../data_raw/"
CLEAN_PATH = "../data_clean/"

# Make sure clean folder exists
os.makedirs(CLEAN_PATH, exist_ok=True)

# Load all raw files
products=pd.read_csv(RAW_PATH+"products_raw.csv")
customers = pd.read_csv(RAW_PATH + "customers_raw.csv")
orders = pd.read_csv(RAW_PATH + "orders_raw.csv")
order_items = pd.read_csv(RAW_PATH + "order_items_raw.csv")
stores = pd.read_csv(RAW_PATH + "stores_raw.csv")

print(products.shape)
print(customers.shape)
print(orders.shape)
print(order_items.shape)
print(stores.shape)

# for products table

# print(products.info())
# print(products.columns)
# print(products.sample(5))
# print(products[products['name'].isnull()])
# products['unit_price']=products['unit_price'].fillna(0)
# products['name']=products['name'].fillna('undefine')
# print(products.isnull().sum())

# # for strip spaces remove

# print(products.sample(5))
# products['name']=products['name'].str.strip().str.replace(r"\s+"," ")
# products['category']=products['category'].str.strip().str.replace(r"\s+"," ")


# #for capital or title word

# products['name']=products['name'].str.title()
# products['category']=products['category'].str.title()

# # for float value convert int and data type also

# products['unit_price']=products['unit_price'].round().astype(int)
# print(products)

# #Handle missing values (fill or remove)
# products["category"] = (
#     products["category"]
#     .astype(str)          # ensure string
#     .str.strip()          # remove spaces
#     .replace("", pd.NA)   # empty → NaN
#     .fillna("unknown")    # fill NaN
# )


# print(products.info())

# #save these file by clene plateform

# os.makedirs("data_clean", exist_ok=True)

# products.to_csv("data_clean/products.csv", index=False)

# print(os.listdir("data_clean"))


# # customers TABLE clening
# print(customers.info())
# print(customers.sample(10))
# print(customers.isnull().sum())
# customers['age']=customers['age'].fillna(0)
# customers['gender']=customers['gender'].fillna('unknown')
# customers['gender']=customers['gender'].replace({'m':'male','f':'female'})
# customers['age']=customers['age'].replace('-',0)
# customers['age']=customers['age'].replace(' ',0)
# customers['city']=customers['city'].str.strip().replace("",'unknown')
# customers['customer_name']=customers['customer_name'].str.strip().replace("",'unknown')

# customers['age']=customers['age'].replace(0,pd.NA)
# print(customers.sample(10))
# print(customers.isnull().sum())

# customers.to_csv("data_clean/customers.csv", index=False)
# print(os.listdir("data_clean"))

# # cleaning order data in csv

# print(orders.info())

# orders['customer_id']=orders['customer_id'].fillna(0)
# orders['customer_id']=(orders['customer_id'].astype(str).str.strip().replace("",0)).astype(int)
# orders['payment_method']=orders['payment_method'].replace('na','unknown')

# orders['order_date'] = pd.to_datetime(
#     orders['order_date'],
#     errors='coerce'
# )

# orders['payment_method']=orders['payment_method'].str.strip().str.lower().replace(['na', 'not_available', 'unknown', ''],pd.NA)
# orders=orders[orders['order_date'].notna()]
# orders['customer_id']=orders['customer_id'].replace(0,pd.NA)
# orders['customer_id']=orders['customer_id'].fillna(-1).astype(int)
# orders['payment_method']=orders['payment_method'].fillna('unknown')
# orders['payment_method']=orders['payment_method'].astype('category')
# print(orders.sample(10))
# print(orders.dtypes)
# print(orders.isnull().sum())

# orders.to_csv("data_clean/orders.csv", index=False)
# print(os.listdir("data_clean"))

# clean order_items data to csv

print(order_items.info())
print(order_items.shape)
order_items=order_items.dropna(subset='product_id')
order_items=order_items.dropna(subset='unit_price')
order_items['discount']=order_items['discount'].fillna(0).round(2)
order_items['product_id']=order_items['product_id'].astype(int)
order_items['final_prize']=order_items['unit_price']*order_items['quantity']-order_items['discount'].round(2)
order_items = order_items.query("final_prize >= 0")
print(order_items.sample(10))
print(order_items.isnull().sum())
print(order_items.dtypes)

# order_items.to_csv("data_clean/order_items.csv", index=False)
# print(os.listdir("data_clean"))


# #cleaning stores data in csv

# print(stores.shape)
# print(stores.info())
# print(stores.isnull().sum())
# stores['state']=stores['state'].replace(['Maharastra','MAHARASHTRA'],'maharashtra')
# stores['state']=stores['state'].fillna('maharashtra')
# stores['city']=stores['city'].str.strip().replace("",'unknown')
# stores['store_name']=stores['store_name'].str.lower().str.replace("-","",regex=False).str.replace(r'\s+'," ",regex=True).str.replace(r"\bd\s+mart\b",'dmart',regex=True).str.strip()
# print(stores['store_name'].unique())


# store_city_map={
#    'dmart thane':'thane',
#    'dmart nagpur':'nagpur',
#    'dmart nashik':'nashik',
#    'dmart mumbai':'mumbai',
#    'dmart pune':'pune'
# }

# stores['city']=stores['store_name'].map(store_city_map).fillna('unknown')

# stores['store_name']=stores['store_name'].fillna('dmart unknown')
# stores['store_name']=stores['store_name'].str.title()
# stores['city']=stores['city'].str.title()
# stores['state']=stores['state'].str.title()
# stores=stores.drop_duplicates(subset=['store_name','city','state'])

# print(stores)

# print(stores.isnull().sum())
# print(stores.dtypes)

# stores.to_csv("data_clean/stores.csv", index=False)
# print(os.listdir("data_clean"))

