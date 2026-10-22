import pandas as pd

#Advanced dataset (10 entries)

hos_data_advanced = [
  ["22:00", "Sys-Maint", "Server_01", "UPDATE_RUN", "10.20.0.5"],
  ["22:10", "Sys_Maint", "Audit_Log", "PURGE", "10.20.0.5"],
  ["01:00", "Root_Admin", "Core_OS", "EXEC_SHELL", "192.168.1.1"],
  ["01:10", "Root_Admin", "Firewall", "DISABLE", "192.168.1.1"],
  ["02:30", "Ext_User", "Archive", "BULK_DL", "198.51.100.4"],
  ["03:00", "EXT_User", "Archive", "BULK_DL", "198.51.100.4"],
  ["03:15", "EXT_User", "Config", "DELETE", "198.51.100.4"],
  ["04:00", "Sys_Maint", "Server_01", "REBOOT", "10.20.0.5"],
  ["04:05", "Sys_Maint", "System", "LOGOUT", "10.20.0.5"],
  ["05:00", "Security", "SIEM", "ALERT", "10.20.0.10"]
]

#Create data fram directly from list data
df = pd.DataFrame(hos_data_advanced, columns=["TIME", "USER", "TARGET", "ACTION", "IP_ADDRESS"])

print("\n--- HOSPITAL ADVANCED SOC INCIDENT LOG ---")

#Print cleanly without index numbers
print(df.to_string(index=False))

