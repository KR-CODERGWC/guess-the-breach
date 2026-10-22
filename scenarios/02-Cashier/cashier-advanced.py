import pandas as pd

#Advanced dataset (10 entries)

cash_adv_data = [
  ["17:00","Cashier_Sam","Reg_01","LOGIN","192.168.10.2"],
  ["17:10","Cashier_Sam","TXN-301","SALE","192.168.10.2"],
  ["17:25","Cashier_Sam","Reg_01","ELEVATE_PRV","192.168.10.2"],
  ["17:26","Cashier_Sam","Safe_Access","BYPASS","192.168.10.2"],
  ["17:30","Cashier_Sam","Safe_Access","DRAIN_DRAWER","192.168.10.2"],
  ["17:40","Cashier_Sam","Audit_Sys","DELETE_LOG","192.168.10.2"],
  ["18:00","Mgr_Karen","Admin_PC","LOGIN","192.168.10.1"],
  ["18:05","Mgr_Karen","Reg_01","AUDIT_FAIL","192.168.10.1"],
  ["18:15","Mgr_Karen","Security","ALERT_PD","192.168.10.1"],
  ["18:30","Mgr_Karen","Admin_PC","LOGOUT","192.168.10.1"]
]

#Create dataframe chart
df = pd.DataFrame(cash_adv_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- CASHIER ADVANCED SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
