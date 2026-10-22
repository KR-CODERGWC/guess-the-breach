import pandas as pd

# Academic Intermediate Dataset (8 entires)

aca_int_data = [
  ["14:00","Prof_Davis","Exams","DOWNLOAD","10.5.2.11"],
  ["14:30","Prof_Davis","Student_A","EDIT_GRADE","10.5.2.11"],
  ["15:00","Prof_Davis","Student_B","EDIT_GRADE","45.72.11.5"],
  ["15:10","Student_Joe","Assignment","SUBMIT","10.5.12.80"],
  ["16:00","Admin_Staff","Payroll","VIEW","10.5.2.20"],
  ["22:15","Student_Joe","Gradebook","ACCESS","10.5.12.80"],
  ["22:20","Student_Joe","Gradebook","MOD_FINAL","10.5.12.80"],
  ["23:00","Student_Joe","Payroll","VIEW_ALL","10.5.12.80"]
]

#Create dataframe chart
df = pd.DataFrame(aca_int_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- ACADEMIC INTERMEDIATE SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
