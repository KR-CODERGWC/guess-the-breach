import pandas as pd

# Corporate Remote Work Advanced Dataset (10 entries)

vpn_adv_data = [
  ["01:00", "Attacker", "VPN_Gateway", "STOLEN_MFA", "198.51.100.9"], # [BREACH 1]: Stolen MFA token usage
  ["01:05", "Attacker", "Domain_Ctrl", "CREATE_ADMIN", "172.16.50.99"], # [BREACH 2]: Backdoor admin account creation
  ["01:10", "Attacker", "Email_Svr", "SPOOF_EXEC", "172.16.50.99"], # [BREACH 3]: Executive email spoofing
  ["01:20", "Attacker", "Finance_DB", "QUERY", "172.16.50.99"], # [BREACH 4]: Unauthorized finance database query
  ["01:30", "Attacker", "Exfil_Node", "SPLIT_TUNNEL", "198.51.100.9"], # [BREACH 5]: Split-tunnel data exfiltration
  ["01:35", "Attacker", "Audit_Logs", "WIPE", "172.16.50.99"], # [BREACH 6]: Audit log wiping
  ["02:00", "SIEM_AI", "Security", "ALERT_BREACH", "172.16.0.5"],
  ["02:10", "Incident_Team", "Gateway", "REVOKE_ALL", "172.16.0.5"],
  ["03:00", "Forensics", "DC_Server", "AUDIT_USERS", "172.16.0.10"],
  ["05:00", "CISO", "Management", "BRIEFING", "172.16.0.2"]
]

#Create dataframe chart
df = pd.DataFrame(vpn_adv_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- CORPOORATE REMOTE WORK (VPN) ADVANCED SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
