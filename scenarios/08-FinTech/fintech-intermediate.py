import pandas as pd

#FinTech Intermediate Dataset (8 entries)

ft_int_data = [
    ["02:00", "Bot_Script", "API_Gateway", "TEST_CARDS", "198.51.100.22"],
    ["02:01", "Bot_Script", "Transfer", "MICRO_TX_01", "198.51.100.22"], 
    ["02:02", "Bot_Script", "Transfer", "MICRO_TX_02", "198.51.100.22"], 
    ["02:03", "Bot_Script", "Transfer", "MICRO_TX_03", "198.51.100.22"], 
    ["02:04", "Bot_Script", "Transfer", "MICRO_TX_04", "198.51.100.22"], 
    ["02:05", "Fraud_Engine", "Alert_Sys", "FLAG_SALAMI", "10.0.0.99"],
    ["02:10", "Security_Sys", "Account_Lock", "FREEZE_ALL", "10.0.0.99"],
    ["03:00", "Client_Amy", "App_Session", "LOGIN_FAIL", "10.0.10.4"]
]

#Create dataframe chart
df = pd.DataFrame(ft_int_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- FINTECH INTERMEDIATE SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
