import pandas as pd

cash_int_data = [
  ["14:00", "Cashier_Sam", "Reg_02", "LOGIN", "192.168.10.3"],
  ["14:30", "Cashier_Sam", "TXN-105", "SALE", "192.168.10.3"],
  ["14:45", "Mgr_Karen", "Admin_PC", "LOGIN", "192.168.10.1"],
  ["15:00", "Mgr_Karen", "Reg_02", "OVERRIDE", "192.168.10.3"],
  ["15:01", "Mgr_Karen", "Safe_Room", "OPEN", "192.168.10.25"],
  ["15:30", "Cashier_Sam", "TXN-106", "VOID", "192.168.10.3"],
  ["15:35", "Cashier_Sam", "Reg_02", "DRAWER_DROP", "192.168.10.25"],
  ["16:00", "Mgr_Karen", "Admin_PC", "LOGOUT", "192.168.10.1"]
]

#Create dataframe chart
df = pd.DataFrame(cash_int_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- CASHIER INTERMEDIATE SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
