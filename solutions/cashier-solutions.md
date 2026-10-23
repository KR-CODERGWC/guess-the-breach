# 🗝️ Answer Key & Explanations: Cashier POS Security Lab

## 🟢 Beginner Tier Solutions (2 Breaches)
* **Row 4 (12:00) – Unauthorized Register Override**
  * *Action:* `OVERRIDE` on `Reg_01` by `Cashier_Sam`.
  * *Why it was flagged:* Cashiers are restricted to processing standard sales transactions. Executing a supervisory or administrative override requires manager-level credentials.
* **Row 6 (13:00) – Unauthorized Drawer Clearing**
  * *Action:* `EMPTY` of `Drawer_All` by `Cashier_Sam`.
  * *Why it was flagged:* Emptying cash drawers is an administrative function reserved for closing managers or secure vault handlers, not standard cashiers.

---

## 🟡 Intermediate Tier Solutions (4 Breaches)
* **Row 5 (15:01) – Physical Security Violation / Breakroom Subnet Anomaly**
  * *Action:* `OPEN` of `Safe_Room` by `Mgr_Karen` from IP `192.168.10.25`.
  * *Why it was flagged:* IP `192.168.10.25` belongs to the noisy staff breakroom, not the secure administrative office (`192.168.10.1`). Opening a cash safe from a breakroom indicates a severe physical security breach or credential sharing.
* **Row 6 (15:30) – Unauthorized Sale Void**
  * *Action:* `VOID` of transaction by `Cashier_Sam`.
  * *Why it was flagged:* Voids require manager sign-off to prevent internal theft or fraudulent receipt manipulation.
* **Row 7 (15:35) – Subnet Mismatch**
  * *Action:* `DRAWER_DROP` shifting action to the breakroom subnet.
* **Row 8 (18:00) – Unsecured Logout State**
  * *Action:* `LOGOUT` by `Mgr_Karen` while register drawers were actively being altered.

---

## 🔴 Advanced Tier Solutions (6 Breaches)
* **Row 3 (17:25) – Local Privilege Escalation**
  * *Action:* `ELEVATE_PRV` on `Reg_01` by `Cashier_Sam`.
  * *Why it was flagged:* Standard terminal user accounts executing commands to escalate local privileges indicate an active exploit or compromised system configuration.
* **Row 4 (17:26) – Security Control Bypass**
  * *Action:* `BYPASS` of `Safe_Access`.
  * *Why it was flagged:* Circumventing digital access controls on cash safes points directly to malicious internal tampering.
* **Row 5 (17:30) – Financial Theft**
  * *Action:* `DRAIN_DRAWER` by `Cashier_Sam`.
* **Row 6 (17:40) – Defense Evasion / Log Wiping**
  * *Action:* `DELETE_LOG` of `Audit_Sys`.
  * *Why it was flagged:* Deleting audit logs is a classic defense-evasion technique used by insiders to cover up cash drawer theft.
* **Row 8 (18:05) – Audit Consistency Failure**
  * *Action:* `AUDIT_FAIL` flagged by management.
* **Row 9 (18:15) – External Law Enforcement Escalation**
  * *Action:* `ALERT_PD` triggered by `Mgr_Karen`.
