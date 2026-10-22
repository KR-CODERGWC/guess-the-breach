import pandas as pd

cash_beg_data = [
  ["11:00", "Cashier_Sam", "Reg_01", "LOGIN", "192.168.10.2"],
  ["11:15", "Cashier_Sam", "TXN-001", "SALE", "192.168.10.2"],
  ["11:30", "Cashier_Sam", "TXN-002", "SALE", "192.168.10.2"],
  ["12:00", "Cashier_Sam", "Reg_01", "OVERRIDE", "192.168.10.2"],
  ["12:45", "Cashier_Sam", "TXN-003", "SALE", "192.168.10.2"],
  ["13:00", "Cashier_Sam", "Drawer_All", "EMPTY", "192.168.10.2"]
]

#Create dataframe chart
df = pd.DataFrame(cash_beg_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- CASHIER BEGINNER SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
