import pandas as pd

# Airport Intermediate Dataset (8 entries)

air_int_data = [
  ["11:00","Agent_Lee","Gate_B2","LOGIN","10.50.1.10"],
  ["11:15","Agent_Lee","Flight_44","CHECK_IN","10.50.1.10"],
  ["11:30","Maint_Tom","gate_B2","ADD_PASSENGER","10.50.9.10"],
  ["12:00","Maint_Tom","VIP_Lounge","UPGRADE_FC","10.50.9.10"],
  ["13:00","Agent_Lee","Flight_44","CLOSE_GATE","10.50.1.10"],
  ["14:00","Unknown","Baggage_Sys","OVERRIDE","192.168.1.50"],
  ["14:10","Agent_Lee","Gate_B2","LOGOUT","10.50.1.10"],
  ["15:00","Tom_Friend","Boarding_Pass","PRINT","192.168.1.50"],
]


#Create dataframe chart
df = pd.DataFrame(air_int_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- AIRPORT INTERMEDIATE SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
