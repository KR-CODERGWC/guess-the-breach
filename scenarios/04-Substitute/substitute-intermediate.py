import pandas as pd

#Substitute Dataset Intermediate (8 entries)
sub_int_data = [
  ["08:00","Sub_Pat","Portal","LOGIN","10.8.2.202"],
  ["08:15","Sub_Pat","Period_1","ATTENDANCE","10.8.2.202"],
  ["09:30","Sub_Pat","Dist_Budget","VIEW","10.8.2.202"],
  ["10:00","Sub_Pat","Staff_Directory","DOWNLOAD","10.8.2.202"],
  ["11:00","Sub_Pat","Pereiod_3","ATTENDANCE","10.8.2.202"],
  ["12:30","Sub_Pat","Health_Files","VIEW_MEDS","10.8.2.202"],
  ["13:30","Sub_Pat","Admin_Notes","EDIT","10.8.2.202"],
  ["15:00","Sub_Pat","Portal","LOGOUT","10.8.2.202"]
]

#Create dataframe chart
df = pd.DataFrame(sub_int_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- SUBSTITUTE INTERMEDIATE SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
