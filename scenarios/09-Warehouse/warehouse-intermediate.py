import pandas as pd

# E-Commerce Warehouse Intermediate dataset (8 entries)

wh_int_data = [
  ["13:00", "Worker_Leo", "Zone_A", "SCAN_BOX", "10.100.4.15"],
  ["13:45", "Manager_Bob", "Inventory_DB", "EDIT_COUNT", "10.100.4.99"], 
  ["14:00", "Manager_Bob", "Inventory_DB", "DELETE_SKU", "10.100.4.99"], 
  ["14:15", "Unknown_IP", "Shipping_API", "GEN_LABEL", "192.168.50.88"],
  ["15:00", "Worker_Mia", "Station_2", "PACK_ORDER", "10.100.4.22"],
  ["16:00", "Forklift_Dan", "Dock_2", "LOAD_VAN", "10.100.4.50"],
  ["16:30", "Manager_Bob", "Inventory_DB", "LOGOUT", "10.100.4.99"],
  ["17:00", "Unknown_IP", "Shipping_API", "BULK_GEN", "192.168.50.88"]
]

#Create dataframe chart
df = pd.DataFrame(wh_int_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- E-COMMERCE WAREHOUSE INTERMEDIATE SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
