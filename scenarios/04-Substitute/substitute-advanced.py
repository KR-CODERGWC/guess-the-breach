import pandas as pd

#Substitute Dataset Advanced (10 entries)
sub_adv_data = [
  ["08:00","Sub_Pat","Portal","LOGIN","10.8.2.202"],
  ["08:15","Sub_Pat","Period_1","ATTENDANCE","10.8.2.202"],
  ["09:00","Sub_Pat","Admin_Panel","ELEVATE_PRV","10.8.2.202"],
  ["09:05","Sub_Pat","Domain_Ctrl","ADD_ADMIN","10.8.2.202"],
  ["09:30","Sub_Pat","Payroll_DB","EXPORT","10.8.2.202"],
  ["10:00","Sub_Pat","Student_DB","DUMP","10.8.2.202"],
  ["11:15","IT_Security","SIEM","ALERT","10.8.0.5"],
  ["11:30","IT_Security","Sub_Pat","REVOC_ACC","10.8.0.5"],
  ["12:00","IT_Security","Device","QUARENTINE","10.8.0.5"],
  ["15:00","IT_Security","Incident","LOG_CLOSE","10.8.0.5"]
  
]

#Create dataframe chart
df = pd.DataFrame(sub_adv_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- SUBSTITUTE ADVANCED SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
