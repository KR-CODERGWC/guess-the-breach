import pandas as pd

# Smart House Beginner Dataset (6 entries)
sh_beg_data = [
  ["07:00","user_Mom","Thermostat","SET_70F","192.168.2.10"],
  ["07:30","Unknown-Ext","Front_Lock","UNLOCK","45.33.22.10"],
  ["12:00","Hub_System","Garage","STATUS","192.168.2.1"],
  ["13:00","Unknown_Ext","Living_Cam","DISABLE","45.33.22.10"],
  ["18:30","User_Dad","Front_Lock","LOCK","192.168.2.12"],
  ["22:00","Hub_System","Alarm","ARM_AWAY","192.168.2.1"]
]

#Create dataframe chart
df = pd.DataFrame(sh_beg_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- SMART HOME BEGINNER SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
