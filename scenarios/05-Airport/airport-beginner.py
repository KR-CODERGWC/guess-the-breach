import pandas as pd

# Airport Beginner Dataset (6 entries)

air_beg_data = [
  ["06:00","Agent_Lee","Gate_B2","LOGIN","192.168.1.50"],
  ["06:15","Agent_Lee","Flight_11","BOARDING","192.168.1.50"],
  ["07:30","Maint_Tom","Terminal_PC","DIAGNOSTIC","10.50.9.20"],
  ["08:00","Agent_Lee","Flight_12","BOARDING","192.168.1.50"],
  ["09:00","Maint_Tom","Terminal_PC","REPAIR_LOG","10.50.9.20"],
  ["10:00","Agent_Lee","Gate_B2","LOGOUT","192.168.1.50"]
]


#Create dataframe chart
df = pd.DataFrame(air_beg_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- AIRPORT BEGINNER SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
