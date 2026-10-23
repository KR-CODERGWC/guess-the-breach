# 🗝️ Answer Key & Explanations: Law Firm Corporate Espionage Lab

## 🟢 Beginner Tier Solutions (2 Breaches)
* **Row 2 (09:30) – Competitor Scraping Activity**
  * *Action:* `SCRAPE` of `Case_101` by `Competitor_Bot` from IP `92.15.4.1`.
  * *Why it was flagged:* IP `92.15.4.1` is registered to a rival legal firm. Automated scraping attempts from external competitor IPs indicate corporate espionage.
* **Row 4 (11:00) – Competitor File Download**
  * *Action:* `DOWNLOAD` by `Competitor_Bot`.

---

## 🟡 Intermediate Tier Solutions (4 Breaches)
* **Row 3 (10:31) – Email Spoofing & Phishing Vector**
  * *Action:* `PHISH_CLICK` on `Email_Svc` from IP `92.15.4.1`.
  * *Why it was flagged:* An executive email communication was intercepted or spoofed via a phishing link originating from a known competitor network.
* **Row 6 (02:15) – Bulk Data Exfiltration**
  * *Action:* `BULK_DL` of `Merger_X` from IP `92.15.4.1`.
  * *Why it was flagged:* Massive file downloading in the middle of the night (2:15 AM) to a competitor IP indicates active **Data Exfiltration**.
* **Row 7 (02:20) – File Sabotage**
  * *Action:* `DELETE` of merger documents by competitor IP.
* **Row 8 (03:00) – Unsupervised Active Session**
  * *Action:* `LOGOUT` delayed on unsupervised terminal.

---

## 🔴 Advanced Tier Solutions (6 Breaches)
* **Row 1 (01:00) – Executive Email Spoofing**
  * *Action:* `SPOOF_EXEC` at `Mail_Gateway` by `Comp_Bot` (`92.15.4.1`).
* **Row 2 (01:02) – Credential Harvesting**
  * *Action:* `HARVEST_CRED` from `Exec_Inboxes`.
* **Row 3 (01:15) – Multi-Factor Authentication Bypass**
  * *Action:* `BYPASS_MFA` on `Merger_Vault`.
  * *Why it was flagged:* Bypassing MFA security gates points to session token hijacking or stolen authentication certificates.
* **Row 4 (01:30) – File Exfiltration**
  * *Action:* `EXFIL_FILES` from `Merger_Vault`.
* **Row 5 (02:00) – Defense Evasion (Log Wiping)**
  * *Action:* `WIPE` of `Audit_Logs`.
* **Row 8 (09:00) – Breach Discovery (Error 404)**
  * *Action:* `ERROR_404` encountered by `Partner_Sara` upon attempting to open missing merger files.
