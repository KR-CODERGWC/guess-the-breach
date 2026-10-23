import pandas as pd

#FinTech Beginner Dataset (6 entries)

ft_beg_data = [
["10:00","Client_Amy","Account-View","BALANCE","10.0.10.4"],
["10:05","Client_Amy","Transfer","SEND_25","10.0.10.4"],
["11:00","Bot_Script","Transfer","MICRO_TX_01","198.51.100.22"],
["12:00","Client_Amy","Bill_Pay","PAY_UTIL","10.0.10.4"],
["13:30","Bot_Script","Transfer","MICRO_TX_02","198.51.100.22"],
["14:00","Client_Amy","App_Session","LOGOUT","10.0.10.4"],
]

#Create dataframe chart
df = pd.DataFrame(ft_beg_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- FINTECH BEGINNER SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
