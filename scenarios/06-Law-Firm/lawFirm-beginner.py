import pandas as pd

#Law Firm Beginner Dataset (6 entries)

law_beg_data = [
  ["09:00", "Partner_Sara", "Case_101", "VIEW", "172.10.1.5"],
  ["09:30", "Competitor_Bot", "Case_101", "SCRAPE", "92.15.4.1"],
  ["10:15", "Partner_Sara", "CASE_102", "REVIEW", "172.10.1.5"],
  ["11:00", "Competitor_Bot", "Case_102", "DOWNLOAD", "92.15.4.1"],
  ["13:00", "Partner_Sara", "Case_101", "SIGN_OFF", "172.10.1.5"],
  ["17:00", "Partner_Sara", "Portal", "LOGOUT", "172.10.1.5"]
]

#Create dataframe chart
df = pd.DataFrame(law_beg_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- LAW FIRM BEGINNER SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
