# 🗝️ Answer Key & Explanations: FinTech Mobile Banking Lab

## 🟢 Beginner Tier Solutions (2 Breaches)
* **Row 3 (11:00) – Unauthorized Micro-Transaction Test**
  * *Action:* `MICRO_TX_01` by `Bot_Script` from IP `198.51.100.22`.
  * *Why it was flagged:* External IP addresses attempting micro-transfers during user sessions indicate automated bot testing of credit limits.
* **Row 5 (13:30) – Second Micro-Transaction Test**
  * *Action:* `MICRO_TX_02` by `Bot_Script`.

---

## 🟡 Intermediate Tier Solutions (4 Breaches)
* **Rows 2–5 (02:01–02:04) – Salami Attack Execution**
  * *Action:* Series of fractional micro-transfers (`MICRO_TX_01` through `04`) executed by `Bot_Script` (`198.51.100.22`).
  * *Why it was flagged:* A **Salami Attack** involves shaving tiny, seemingly insignificant fractions of money across multiple transactions to siphon funds without triggering major automated withdrawal alarms.
* **Row 6 (02:05) – Fraud Engine Alert**
  * *Action:* `FLAG_SALAMI` triggered by `Fraud_Engine`.
* **Row 7 (02:10) – Emergency Account Freeze**
  * *Action:* `FREEZE_ALL` executed by `Security_Sys`.
* **Row 8 (03:00) – Post-Freeze Login Failure**
  * *Action:* `LOGIN_FAIL` by `Client_Amy`.

---

## 🔴 Advanced Tier Solutions (6 Breaches)
* **Row 1 (03:00) – Session Hijacking**
  * *Action:* `SESSION_HIJACK` by `Attacker` from IP `203.0.113.88`.
* **Row 2 (03:01) – Multi-Factor Authentication Bypass**
  * *Action:* `BYPASS_MFA` on `MFA_Token`.
  * *Why it was flagged:* Bypassing MFA tokens indicates token replay or session cookie theft.
* **Row 3 (03:02) – Wire Transfer Drain**
  * *Action:* `INIT_DRAIN` on `Wire_System`.
* **Row 4 (03:03) – Batch Salami Attack Execution**
  * *Action:* `EXEC_BATCH` of `Salami_Module`.
* **Row 5 (03:04) – Fund Exfiltration to Crypto Bridge**
  * *Action:* `EXFIL_FUNDS` to `Crypto_Bridge`.
  * *Why it was flagged:* Transferring drained capital into decentralized cryptocurrency bridges is a primary method of laundering stolen funds.
* **Row 6 (03:05) – Audit Log Wiping**
  * *Action:* `WIPE` of `Audit_Logs`.
