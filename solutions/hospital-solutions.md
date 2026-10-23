# 🗝️ Answer Key & Explanations: Hospital Security Lab

This document breaks down every anomaly and security breach embedded across the Beginner, Intermediate, and Advanced tiers of the Hospital scenario, explaining why each entry was flagged.

---

## 🟢 Beginner Tier Solutions (2 Breaches)
* **Row 2 (08:15) – Subnet Mismatch / Credential Hijack**
  * *Action:* `MOD_DOSE` by `Dr_Adams` from IP `10.20.5.88`.
  * *Why it was flagged:* Dr. Adams' administrative account is restricted to the doctor office subnet (`10.20.1.x`). Because this action originated from `10.20.5.88` (a nurse station subnet), it indicates either physical credential sharing or workstation hijacking.
* **Row 4 (13:20) – Unauthorized Off-Hours Export**
  * *Action:* `EXPORT` of `Pharmacy_DB` by `Tech_Kyle` from IP `10.20.9.50`.
  * *Why it was flagged:* Technical support personnel are not authorized to export entire pharmaceutical databases outside of scheduled, approved maintenance windows.

---

## 🟡 Intermediate Tier Solutions (4 Breaches)
* **Row 3 (14:05) – Subnet Mismatch** *(Same as Beginner)*
* **Row 4 (16:30) – Unauthorized Database Export** *(Same as Beginner)*
* **Row 5 (23:15) – Impossible Travel / Location Discrepancy**
  * *Action:* `ACCESS` by `Dr_Adams` from IP `10.20.1.15` at midnight.
  * *Why it was flagged:* Dr. Adams is officially confirmed to be on a medical convention trip in Hawaii this week. Local badge/network access occurring at midnight directly conflicts with physical travel records.
* **Row 8 (18:00) – Unauthorized Admin Check**
  * *Action:* `CHECK` by `Admin` from IP `10.20.1.1`.
  * *Why it was flagged:* Administrative checks executed outside of standard operating parameters or shift rosters require secondary verification and log auditing.

---

## 🔴 Advanced Tier Solutions (6 Breaches)
* **Row 2 (22:10) – Trojan Horse Log Purge**
  * *Action:* `PURGE` of `Audit_Log` by `Sys_Maint` from IP `10.20.0.5`.
  * *Why it was flagged:* A routine system update script acted as a **Trojan Horse**, silently deleting audit logs to cover up subsequent unauthorized intrusion tracks.
* **Rows 3–4 (01:00–01:10) – Privilege Escalation & Defense Evasion**
  * *Action:* `EXEC_SHELL` and `DISABLE` firewall by `Root_Admin` from IP `192.168.1.1`.
  * *Why it was flagged:* Unidentified external IP executing root shell commands and disabling core firewall defenses represents active system takeover.
* **Rows 5–6 (02:30–03:00) – Data Exfiltration**
  * *Action:* Bulk download (`BULK_DL`) of patient archives by `Ext_User` from IP `198.51.100.4`.
  * *Why it was flagged:* Massive outbound data transfers to an external, unverified IP address indicate active **Data Exfiltration** of sensitive Protected Health Information (PHI).
* **Row 7 (03:15) – System Sabotage**
  * *Action:* `DELETE` of configuration files by `Ext_User`.
  * *Why it was flagged:* Unauthorized deletion of core system configurations is a malicious sabotage tactic designed to prevent system recovery.
