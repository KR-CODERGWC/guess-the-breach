# 🗝️ Answer Key & Explanations: Corporate Remote Work VPN Lab

## 🟢 Beginner Tier Solutions (2 Breaches)
* **Row 3 (10:00) – Unverified IP Connection**
  * *Action:* `CONNECT` to `VPN_Gateway` from IP `203.0.113.42` under user `Emp_Zack`.
  * *Why it was flagged:* Connection originates from an unrecognized external IP address inconsistent with Zack's standard remote profile.
* **Row 5 (12:30) – Domain Controller Authentication Failure**
  * *Action:* `AUTH_FAIL` on `DC_Server` from unverified IP `203.0.113.42`.

---

## 🟡 Intermediate Tier Solutions (4 Breaches)
* **Row 3 (10:20) – Email Spoofing Attack Vector**
  * *Action:* `SPOOF_IT` on `Mail_Gateway` by `Phishing_Svr` (`198.51.100.9`).
* **Row 5 (11:12) – Impossible Travel Login**
  * *Action:* `CONNECT` to `VPN_Gateway` from IP `203.0.113.99`.
  * *Why it was flagged:* **Impossible Travel** occurs when the same employee account successfully authenticates from two geographically distant locations within an impossible timeframe (e.g., New York and Tokyo 12 minutes apart).
* **Row 6 (11:15) – Domain Controller Auth Failure**
  * *Action:* `AUTH_FAIL` on `DC_Server`.
* **Row 7 (12:00) – SecOps Impossible Travel Alert**
  * *Action:* `IMPOSSIBLE_TRAVEL` alert triggered by `SecOps`.

---

## 🔴 Advanced Tier Solutions (6 Breaches)
* **Row 1 (01:00) – Stolen MFA Token Login**
  * *Action:* `STOLEN_MFA` authentication at `VPN_Gateway` (`198.51.100.9`).
* **Row 2 (01:05) – Backdoor Administrator Creation**
  * *Action:* `CREATE_ADMIN` on `Domain_Ctrl` (`172.16.50.99`).
  * *Why it was flagged:* Attackers establishing administrative accounts ensure persistent access even if user passwords are changed.
* **Row 3 (01:10) – Executive Email Spoofing**
  * *Action:* `SPOOF_EXEC` on `Email_Svr`.
* **Row 4 (01:20) – Unauthorized Finance Database Query**
  * *Action:* `QUERY` on `Finance_DB`.
* **Row 5 (01:30) – Split-Tunnel Data Exfiltration**
  * *Action:* `SPLIT_TUNNEL` to `Exfil_Node` (`198.51.100.9`).
  * *Why it was flagged:* Split-tunneling routes corporate data out to external unauthorized servers while bypassing enterprise security gateways.
* **Row 6 (01:35) – Audit Log Wiping**
  * *Action:* `WIPE` of `Audit_Logs`.
