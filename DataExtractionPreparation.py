import pandas as pd
import numpy as np
import tableauserverclient as TSC

# Extract data from multiple sources
def prepare_tableau_data():
    # Read from multiple sources
    sql_data = pd.read_sql_query("SELECT * FROM sales_table", connection)
    csv_data = pd.read_csv('customer_data.csv')
    
    # Data cleaning and transformation
    merged_data = pd.merge(sql_data, csv_data, on='customer_id')
    
    # Feature engineering
    merged_data['total_revenue'] = merged_data['price'] * merged_data['quantity']
    
    # Prepare for Tableau export
    merged_data.to_csv('tableau_ready_data.csv', index=False)
