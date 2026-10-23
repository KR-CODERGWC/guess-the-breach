import pandas as pd

# E-Commerce Warehouse Beginner dataset (6 entries)

wh_beg_data = [
  ["08:00", "Worker_Leo", "Zone_A", "SCAN_BOX", "10.100.4.15"],
  ["08:30", "Manager_Bob", "Inventory_DB", "DELETE_SKU", "10.100.4.99"], 
  ["09:15", "Worker_Leo", "Zone_B", "SCAN_BOX", "10.100.4.15"],
  ["10:00", "Unknown_IP", "Shipping_API", "GEN_LABEL", "192.168.50.88"], 
  ["11:30", "Worker_Mia", "Station_2", "BREAK", "10.100.4.22"],
  ["12:00", "Worker_Leo", "Station_1", "LOGOUT", "10.100.4.15"]
]

#Create dataframe chart
df = pd.DataFrame(wh_beg_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- E-COMMERCE WAREHOUSE BEGINNER SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
