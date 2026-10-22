import pandas as pd

#Academic Advanced Dataset (10 entires)

aca_adv_data = [
  ["01:00","Bot_Script","DB_Connect","INIT","192.168.1.105"],
  ["01:02","Bot_Script","GPA_Table","SELECT_ALL","192.168.1.105"],
  ["01:05","Bot_Script","SSN_Vault","DUMP","192.168.1.105"],
  ["01:10","Bot_Script","Admin_Table","DROP","192.168.1.105"],
  ["01:15","Bot_Script","Exfil_Server","UPLOAD_ZIP","192.168.1.105"],
  ["02:00","SOC_Alert","SIEM","TRIGGER","10.5.0.2"],
  ["02:10","SecOps_Lead","FireWall","BLOCK_IP","10.5.0.10"],
  ["02:15","SecOps_Lead","DB_Server","SNAPSHOT","10.5.0.10"],
  ["03:00","SecOps_Lead","Incident_Log","CLOSE","10.5.0.10"],
  ["03:05","SecOps_Lead","System","LOGOUT","10.5.0.10"]
]

#Create dataframe chart
df = pd.DataFrame(aca_adv_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- ACADEMIC ADVANCED SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
