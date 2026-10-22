import pandas as pd

# Airport Advanced Dataset (10 entries)

air_adv_data = [
  ["23:00","Unknown","Control_Tower","ACCESS","192.168.1.50"],
  ["23:05","Unknown","Flight_Plan","CREATE_GHOST","192.168.1.50"],
  ["23:15","Unknown","Radar_Sys","DISABLE","192.168.1.50"],
  ["23:30","FAA_Monitor","Alert_Sys","TRIGGER","10.50.0.1"],
  ["23:35","SecOps","Gateway","BLOCK_GUEST","10.50.0.5"],
  ["23:40","SecOps","Tower_Link","ISOLATE","10.50.0.5"],
  ["00:00","Admin","Backup_Sys","RESTORE","10.50.0.2"],
  ["00:15","Admin","Radar_Sys","RE-ENABLE","10.50.0.2"],
  ["01:00","Admin","Audit","EXPORT_LOGS","10.50.0.2"],
  ["01:30","Admin","System","SECURE_ALL","10.50.0.2"]
]

#Create dataframe chart
df = pd.DataFrame(air_adv_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- AIRPORT ADVANCED SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
