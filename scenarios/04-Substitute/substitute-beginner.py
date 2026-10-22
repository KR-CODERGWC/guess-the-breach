import pandas as pd

#Substitute Dataset Beginner (6 entries)
sub_beg_data = [
  ["08:00","Sub_Pat","Portal","LOGIN","10.8.2.202"],
  ["08:15","Sub_Pat","Period_1","ATTENDANCE","10.8.2.202"],
  ["09:00","Sub_Pat","Dist_Budget","VIEW","10.8.2.202"],
  ["10:15","Sub_Pat","Period_2","ATTENDANCE","10.8.2.202"],
  ["11:00","Sub_Pat","Staff_Pay","ACCESS","10.8.2.202"],
  ["15:00","Sub_Pat","Portal","LOGOUT","10.8.2.202"],
]

#Create dataframe chart
df = pd.DataFrame(sub_beg_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- SUBSTITUTE BEGINNER SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
