import pandas as pd

#FinTech Advanced Dataset (10 entries)

ft_adv_data = [
  ["03:00", "Attacker", "Auth_Service", "SESSION_HIJACK", "203.0.113.88"], 
    ["03:01", "Attacker", "MFA_Token", "BYPASS_MFA", "203.0.113.88"], 
    ["03:02", "Attacker", "Wire_System", "INIT_DRAIN", "203.0.113.88"],
    ["03:03", "Attacker", "Salami_Module", "EXEC_BATCH", "203.0.113.88"], 
    ["03:04", "Attacker", "Crypto_Bridge", "EXFIL_FUNDS", "203.0.113.88"], 
    ["03:05", "Attacker", "Audit_Logs", "WIPE", "203.0.113.88"], 
    ["03:10", "SecOps_Auto", "Core_Bank", "EMERGENCY_LOCK", "10.0.0.99"],
    ["04:00", "SecOps_Lead", "Forensics", "PULL_LOGS", "10.0.0.15"],
    ["05:00", "SecOps_Lead", "Compliance", "FILE_SAR", "10.0.0.15"],
    ["06:00", "Executive", "Board", "BRIEFING", "10.0.0.2"]
]

#Create dataframe chart
df = pd.DataFrame(ft_adv_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- FINTECH ADVANCED SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
