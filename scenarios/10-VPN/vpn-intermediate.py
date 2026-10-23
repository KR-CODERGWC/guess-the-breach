import pandas as pd

# Corporate Remote Work Intermediate Dataset (8 entries)

vpn_int_data = [
  ["10:00", "Emp_Zack", "VPN_Gateway", "CONNECT", "172.16.50.20"],
  ["10:15", "Emp_Zack", "HR_Portal", "VIEW", "172.16.50.20"],
  ["10:20", "Phishing_Svr", "Mail_Gateway", "SPOOF_IT", "198.51.100.9"], 
  ["11:00", "Emp_Zack", "VPN_Gateway", "DISCONNECT", "172.16.50.20"],
  ["11:12", "Emp_Zack", "VPN_Gateway", "CONNECT", "203.0.113.99"], 
  ["11:15", "Emp_Zack", "DC_Server", "AUTH_FAIL", "203.0.113.99"], 
  ["12:00", "SecOps", "Alert_Sys", "IMPOSSIBLE_TRAVEL", "172.16.0.2"], 
  ["12:05", "SecOps", "Emp_Zack", "FORCE_LOGOUT", "172.16.0.2"]
]

#Create dataframe chart
df = pd.DataFrame(vpn_int_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- CORPOORATE REMOTE WORK (VPN) INTERMEDIATE SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
