# DMART Project

A data analytics project simulating DMART operations, including raw data, cleaning scripts, MySQL integration, and dashboards.

---

## Project Structure

DMART_PROJECT/
│
├── data_raw/ # Raw CSV data files
│ ├── customers_raw.csv
│ ├── order_items_raw.csv
│ ├── orders_raw.csv
│ └── products_raw.csv
│
├── scripts/ # Data cleaning and loading scripts
│ ├── data_clean/ # Folder for intermediate cleaning scripts
│ ├── cleaning.py # Script to clean raw data
│ ├── load_to_mysql.py # Script to load cleaned data into MySQL
│ ├── mysql_connector.py # MySQL connection helper
│ └── init.py
│
├── dashboards/ # Superset or other dashboard files
│ ├── superset_dashboard.html
│ └── other_dashboard_files
│
├── dmart_architecture.drawio # Architecture diagram
└── README.md # Project overview


---

## Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/KrushnaP24/DMART_PROJECT.git
cd DMART_PROJECT

python -m venv .venv
.venv\Scripts\activate   # Windows
# or for Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt

##for dashbord view
![Dashboard Preview](https://raw.githubusercontent.com/USERNAME/REPO_NAME/main/assets/dashboard.png)

