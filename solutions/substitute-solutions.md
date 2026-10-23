# 🗝️ Answer Key & Explanations: Substitute Teacher Access Lab

## 🟢 Beginner Tier Solutions (2 Breaches)
* **Row 3 (09:00) – Least-Privilege Violation (District Budget)**
  * *Action:* `VIEW` of `Dist_Budget` by `Sub_Pat`.
  * *Why it was flagged:* Substitute teachers are restricted to classroom attendance and lesson plans on the student VLAN (`10.8.2.202`). Accessing district financial budgets violates the principle of least privilege.
* **Row 5 (11:00) – Staff Payroll Access**
  * *Action:* `ACCESS` of `Staff_Pay` by `Sub_Pat`.

---

## 🟡 Intermediate Tier Solutions (4 Breaches)
* **Row 3 (09:30) – District Budget Access** *(Same as Beginner)*
* **Row 4 (10:00) – Unauthorized Directory Download**
  * *Action:* `DOWNLOAD` of `Staff_Directory` by `Sub_Pat`.
  * *Why it was flagged:* Downloading internal staff contact directories exceeds substitute teaching operational scope.
* **Row 6 (12:30) – Medical Privacy Violation (FERPA/HIPAA)**
  * *Action:* `VIEW_MEDS` of `Health_Files` by `Sub_Pat`.
  * *Why it was flagged:* Student medical files and medication logs are legally protected confidential records that unauthorized substitutes cannot view.
* **Row 7 (13:30) – Unauthorized Administrative Note Editing**
  * *Action:* `EDIT` of `Admin_Notes` by `Sub_Pat`.

---

## 🔴 Advanced Tier Solutions (6 Breaches)
* **Row 3 (09:00) – Privilege Escalation**
  * *Action:* `ELEVATE_PRV` in `Admin_Panel` by `Sub_Pat`.
  * *Why it was flagged:* Low-privilege accounts executing commands to escalate permissions point to internal system compromise.
* **Row 4 (09:05) – Backdoor Account Creation**
  * *Action:* `ADD_ADMIN` in `Domain_Ctrl` by `Sub_Pat`.
  * *Why it was flagged:* Creating new administrator accounts guarantees persistent unauthorized access.
* **Row 5 (09:30) – Payroll Data Export**
  * *Action:* `EXPORT` of `Payroll_DB`.
* **Row 6 (10:00) – Student Database Dump**
  * *Action:* `DUMP` of `Student_DB`.
* **Row 8 (11:30) – Account Revocation**
  * *Action:* `REVOKE_ACC` by `IT_Security`.
* **Row 9 (12:00) – Device Quarantine**
  * *Action:* `QUARANTINE` of compromised endpoint.
