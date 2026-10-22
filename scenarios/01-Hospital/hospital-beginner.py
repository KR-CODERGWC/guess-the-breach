import pandas as pd

# Beginner dataset (6 entries)
hos_data_beginner = [
  ["08:00","Dr_Adams","P_101","VIEW_CHART","10.20.1.15"],
  ["08:15","Dr_Adams","P_102","MOD_DOSE","10.20.5.88"],
  ["09:30","Nurse_Beth","P_103","DISPENSE","10.20.5.20"],
  ["13:20","Tech_Kyle","Pharmacy_DB","EXPORT","10.20.9.50"],
  ["15:00","Nurse_Beth","P_104","VIEW_CHART","10.20.5.20"],
  ["17:00","Dr_Adams","SYSTEM","LOGOUT","10.20.1.15"],
]


#create DataFrame directly from your list data
df = pd.DataFrame(hos_data_beginner, columns=["TIME", "USER", "TARGET", "ACTION", "IP_ADDRESS"])

#Print Beginner Log Title
print("\n--- HOSPITAL BEGINNER SOC INCIDENT LOG --")
                  
#Print cleanly without index numbers
print(df.to_string(index=False))
