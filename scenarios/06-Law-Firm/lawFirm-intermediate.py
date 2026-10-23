import pandas as pd

#Law Firm Intermediate Dataset (8 entries)

law_int_data = [
  ["10:00", "Partner_Sara", "Merger_X", "VIEW", "172.10.1.5"],
  ["10:30", "Exec_Director", "Email_Svc", "SEND_DOC", "172.10.1.2"],
  ["10:31", "Spoofed_Sender", "Email_Svc", "PHISH_CLICK", "92.15.4.1"],
  ["11:00", "Para_Tim", "Merger_X", "EXPORT", "172.10.1.5"],
  ["12:00", "Partner_Sara", "Merger_X", "EDIT", "172.10.1.5"],
  ["02:15", "Para_Tim", "Merger_X", "BULK_DL", "92.15.4.1"],
  ["02:20", "Para_Tim", "Merger_X", "DELETE", "92.15.4.1"],
  ["03:00", "Partner_Sara", "Portal", "LOGOUT", "172.10.1.5"]
]

#Create dataframe chart
df = pd.DataFrame(law_int_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- LAW FIRM INTERMEDIATE SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
