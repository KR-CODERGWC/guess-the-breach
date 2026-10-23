# 🗝️ Answer Key & Explanations: Academic Integrity Lab

## 🟢 Beginner Tier Solutions (2 Breaches)
* **Row 3 (10:00) – Unauthorized Student Roster Access**
  * *Action:* `VIEW` of `Roster` by `Student_Joe`.
  * *Why it was flagged:* Students have zero administrative authority to view class rosters containing peer identification data.
* **Row 5 (12:00) – Grade Modification by Student**
  * *Action:* `MOD_GRADE` in `Gradebook` by `Student_Joe`.
  * *Why it was flagged:* Gradebook modification rights belong strictly to faculty members (`Prof_Davis`), making student edits a severe breach of academic integrity.

---

## 🟡 Intermediate Tier Solutions (4 Breaches)
* **Row 3 (15:00) – Geo-IP / VPN Anomaly**
  * *Action:* `EDIT_GRADE` by `Prof_Davis` from IP `45.72.11.5`.
  * *Why it was flagged:* Professor Davis is on an overseas sabbatical in London with unreliable connectivity, yet this specific traffic routes through a commercial proxy/VPN exit node rather than expected campus subnets (`10.5.2.x`).
* **Row 6 (22:15) – Off-Hours Gradebook Access**
  * *Action:* `ACCESS` by `Student_Joe` at late hours.
* **Row 7 (22:20) – Final Grade Alteration**
  * *Action:* `MOD_FINAL` by `Student_Joe`.
* **Row 8 (23:00) – Unauthorized Payroll Inspection**
  * *Action:* `VIEW_ALL` of `Payroll` by `Student_Joe`.

---

## 🔴 Advanced Tier Solutions (6 Breaches)
* **Row 2 (01:02) – Unauthorized Database Query**
  * *Action:* `SELECT_ALL` of `GPA_Table` by `Bot_Script` (`192.168.1.105`).
  * *Why it was flagged:* Automated scripts executing bulk data queries from external proxy IPs indicate database harvesting.
* **Row 3 (01:05) – Data Exfiltration (SSN Dump)**
  * *Action:* `DUMP` of `SSN_Vault` by `Bot_Script`.
  * *Why it was flagged:* Accessing and dumping Social Security Number vaults represents severe Protected Information leakage.
* **Row 4 (01:10) – System Sabotage (Database Drop)**
  * *Action:* `DROP` of `Admin_Table` by `Bot_Script`.
  * *Why it was flagged:* Executing SQL `DROP TABLE` commands destroys core database structure, a destructive cyberattack pattern.
* **Row 5 (01:15) – Exfiltration Upload**
  * *Action:* `UPLOAD_ZIP` to `Exfil_Server`.
* **Row 8 (02:15) – Incident Response Recovery (Snapshot)**
  * *Action:* `SNAPSHOT` by `SecOps_Lead`.
* **Row 10 (03:05) – Incident Closure**
  * *Action:* `LOGOUT` by `SecOps_Lead`.
