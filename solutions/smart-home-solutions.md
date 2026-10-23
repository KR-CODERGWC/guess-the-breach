# 🗝️ Answer Key & Explanations: Smart Home / IoT Hub Security Lab

## 🟢 Beginner Tier Solutions (2 Breaches)
* **Row 2 (07:30) – Unauthorized External Lock Manipulation**
  * *Action:* `UNLOCK` of `Front_Lock` by `Unknown_Ext` from IP `45.33.22.10`.
  * *Why it was flagged:* External IPs (`45.33.22.10`) outside the local home subnet (`192.168.2.x`) should never execute physical lock commands.
* **Row 4 (13:00) – External Camera Deactivation**
  * *Action:* `DISABLE` of `Living_Cam` by external IP.

---

## 🟡 Intermediate Tier Solutions (4 Breaches)
* **Row 2 (13:15) – Unauthorized Remote Unlock** *(Same as Beginner)*
* **Row 3 (13:16) – Camera Feed Disabled** *(Same as Beginner)*
* **Row 4 (14:00) – Camera Error Response**
  * *Action:* `ERROR` returned during `Front_Cam` check by `User_Dad`.
  * *Why it was flagged:* Camera feed failures following external interference indicate hardware tampering or offline status caused by intruders.
* **Row 6 (18:30) – Lock Status Failure**
  * *Action:* `FAIL` returned on `Front_Lock` status query.

---

## 🔴 Advanced Tier Solutions (6 Breaches)
* **Row 1 (02:00) – Trojan Firmware Modification**
  * *Action:* `FIRMWARE_MOD` on `Master_Hub` by `Botnet_Node` (`185.159.4.2`).
  * *Why it was flagged:* Malicious firmware patches overwrite legitimate hub operating code to establish permanent backdoor control.
* **Row 2 (02:01) – Camera Deactivation**
  * *Action:* `OFF` command sent to `All_Cameras`.
* **Row 3 (02:02) – Smart Lock Compromise**
  * *Action:* `UNLOCK` command sent to `All_Locks`.
* **Row 4 (02:05) – Encryption Key Exfiltration**
  * *Action:* `UPLOAD_KEYS` to `Exfil_Server`.
  * *Why it was flagged:* Exporting local device encryption keys allows attackers to clone access credentials.
* **Row 5 (06:00) – Morning Hub Status Error**
  * *Action:* `ERROR` logged by `User_Mom`.
* **Row 8 (07:15) – Emergency Factory Reset**
  * *Action:* `FACTORY_RESET` executed by `User_Dad` to purge compromised firmware.
