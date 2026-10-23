import pandas as pd

#Law Firm Advanced Dataset (10 entries)

law_adv_data = [
  ["01:00", "Comp_Bot", "Mail_Gateway", "SPOOF_EXEC", "92.15.4.1"],
  ["01:02", "Comp_Bot", "Exec_Inboxes", "HARVEST_CRED", "92.15.4.1"],
  ["01:15", "Comp_Bot", "Merger_Vault", "BYPASS_MFA", "92.15.4.1"],
  ["01:30", "Comp_Bot", "Merger_Vault", "EXFIL_FILES", "92.15.4.1"],
  ["02:00", "Comp_Bot", "Audit_logs", "WIPE", "92.15.4.1"],
  ["08:00", "IT_Lead", "Mail_Server", "DETECT_SPOOF", "172.10.0.5"],
  ["08:30", "IT_Lead", "Firewall", "BAN_IP", "172.10.0.5"],
  ["09:00", "Partner_Sara", "Merger_Vault", "ERROR_404", "172.10.1.5"],
  ["09:15", "Partner_sara", "Security", "REPORT_BREACH", "172.10.1.5"],
  ["10:00", "Forensics", "Server_01", "IMAGE_DRIVE", "172.10.0.10"]
]

#Create dataframe chart
df = pd.DataFrame(law_adv_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- LAW FIRM ADVANCED SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
