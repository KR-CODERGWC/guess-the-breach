import pandas as pd

# Smart House Intermediate Dataset (8 entries)
sh_int_data = [
  ["13:00","User_Mom","Thermostat","SET_72F","192.168.2.10"],
  ["13:15","Unknown_Ext","Front_Lock","UNLOCK","45.33.22.10"],
  ["13:16","Unknown_Ext","Living_Cam","DISABLE","45.33.22.10"],
  ["14:00","User_Dad","Front_Cam","CHECK","192.168.2.12"],
  ["17:00","User_Mom","Living_Lights","ON","192.168.2.10"],
  ["18:30","User_Dad","Front_Lock","STATUS","192.168.2.12"],
  ["21:00","User_Dad","Hub_System","REBOOT","192.168.2.12"],
  ["22:00","Hub_System","Alarm","ARM_AWAY","192.168.2.1"]
]

#Create dataframe chart
df = pd.DataFrame(sh_int_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- SMART HOME INTERMEDIATE SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
