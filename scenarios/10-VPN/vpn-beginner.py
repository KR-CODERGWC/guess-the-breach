import pandas as pd

# Corporate Remote Work Beginner Dataset (6 entries)

vpn_beg_data = [
  ["08:30", "Emp_Zack", "VPN_Gateway", "CONNECT", "172.16.50.20"],
  ["08:45", "Emp_Zack", "Email_Svc", "SYNC", "172.16.50.20"],
  ["10:00", "Emp_Zack", "VPN_Gateway", "CONNECT", "203.0.113.42"], 
  ["12:00", "Emp_Nora", "VPN_Gateway", "CONNECT", "172.16.50.25"],
  ["12:30", "Emp_Zack", "DC_Server", "AUTH_FAIL", "203.0.113.42"], 
  ["17:00", "Emp_Zack", "VPN_Gateway", "DISCONNECT", "203.0.113.42"]
]

#Create dataframe chart
df = pd.DataFrame(vpn_beg_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- CORPOORATE REMOTE WORK (VPN) BEGINNER SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
