import pandas as pd

#Intermediate Dataset (8 entries)

data_intermediate = [
  ["13:00","Dr_Adams","P_201","VIEW_CHART","10.20.1.15"],
  ["13:20","Tech_Kyle","Pharmacy_DB","QUERY","10.20.9.50"],
  ["14:05","Dr_Adams","P_202","MOD_DOSE","10.20.5.88"],
  ["16:30","Tech_Kyle","Pharmacy_DB","EXPORT","10.20.9.50"],
  ["23:15","Dr_Adams","P_901","ACCESS","10.20.1.15"],
  ["17:00","Dr_Adams","SYSTEM","LOGOUT","10.20.1.15"],
  ["17:05","Tech_Kyle","SYSTEM","LOGOUT","10.20.9.50"],
  ["18:00","Admin","System","CHECK","10.20.1.1"]
]

#Create Intermediate Chart
df = pd.DataFrame(data_intermediate, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

#Label Log and chart
print("\n--- HOSPITAL INTERMEDIATE SOC INCIDENT LOG ---")

#Print cleanly without index numbers
print(df.to_string(index=False))
