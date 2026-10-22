import pandas as pd

# Academic Beginner Dataset (6 entires)

aca_beg_data = [
  ["09:00","Prof_Davis","Syllabus","UPLOAD","10.5.2.11"],
  ["09:30","Prof_Davis","Quiz_1","GRADE","10.5.2.11"]
  ["10:00","Student_Joe","Roster","VIEW","10.5.2.11"]
  ["11;15","Prof_Davis","Quiz_1","PUBLISH","10.5.2.11"]
  ["12:00","Student_Joe","Gradebook","MOD_GRADE","10.5.2.11"]
  ["13:00","Prof_Davis","Portal","LOGOUT","10.5.2.11"]
]

#Create dataframe chart
df = pd.DataFrame(aca_beg_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS"])

print("\n--- ACADEMIC BEGINNER SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
