import pandas as pd

# E-Commerce Warehouse Advanced dataset (10 entries)

wh_adv_data = [
  ["22:00", "Insider_Bot", "Warehouse_PC", "EXEC_SCRIPT", "10.100.4.15"], 
  ["22:05", "Insider_Bot", "Batch_System", "REROUTE_ALL", "10.100.4.15"], 
  ["22:10", "Insider_Bot", "Manifest_DB", "WIPE_RECORDS", "10.100.4.15"], 
  ["22:15", "Insider_Bot", "Ext_Server", "EXFIL_MANIFEST", "192.168.50.88"], 
  ["22:20", "Insider_Bot", "Warehouse_PC", "SELF_DESTRUCT", "10.100.4.15"],
  ["23:00", "Logistics_AI", "Monitor", "ANOMALY_DETECT", "10.100.0.2"], 
  ["23:05", "SecOps", "Firewall", "BLOCK_PORT", "10.100.0.5"],
  ["23:15", "SecOps", "Warehouse_PC", "ISOLATE", "10.100.0.5"],
  ["01:00", "Auditor", "Report", "GENERATE", "10.100.0.10"],
  ["02:00", "Auditor", "System", "LOCKDOWN", "10.100.0.10"]
]

#Create dataframe chart
df = pd.DataFrame(wh_adv_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- E-COMMERCE WAREHOUSE ADVANCED SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
