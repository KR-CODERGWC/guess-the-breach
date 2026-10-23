# 🗝️ Answer Key & Explanations: Airport Operations Security Lab

## 🟢 Beginner Tier Solutions (2 Breaches)
* **Row 1 (06:00) – Guest Wi-Fi Network Violation**
  * *Action:* `LOGIN` by `Agent_Lee` from IP `192.168.1.50`.
  * *Why it was flagged:* Internal gate operations must occur over secured internal terminals (`10.50.x.x`). Connecting via `192.168.1.50` indicates the use of unsecured public guest Wi-Fi.
* **Row 6 (10:00) – Guest Network Logout**
  * *Action:* `LOGOUT` from guest Wi-Fi.

---

## 🟡 Intermediate Tier Solutions (4 Breaches)
* **Row 3 (11:30) – Out-of-Scope Task Execution**
  * *Action:* `ADD_PASSENGER` by `Maint_Tom` (`10.50.9.20`).
  * *Why it was flagged:* Maintenance personnel are tasked with hardware repairs, not modifying passenger flight manifests.
* **Row 4 (12:00) – Unauthorized First-Class Upgrade**
  * *Action:* `UPGRADE_FC` in `VIP_Lounge` by `Maint_Tom`.
* **Row 6 (14:00) – Baggage System Override via Guest Wi-Fi**
  * *Action:* `OVERRIDE` of `Baggage_Sys` from IP `192.168.1.50`.
  * *Why it was flagged:* Critical baggage tracking systems must never be modified from external guest networks.
* **Row 8 (15:00) – Unauthorized Boarding Pass Print**
  * *Action:* `PRINT` of `Boarding_Pass` from guest Wi-Fi.

---

## 🔴 Advanced Tier Solutions (6 Breaches)
* **Row 1 (23:00) – Unauthorized Tower Access**
  * *Action:* `ACCESS` of `Control_Tower` from IP `192.168.1.50`.
* **Row 2 (23:05) – Ghost Flight Creation**
  * *Action:* `CREATE_GHOST` of `Flight_Plan`.
  * *Why it was flagged:* Injecting unverified ghost flights into airspace tracking systems introduces extreme aviation safety hazards.
* **Row 3 (23:15) – Critical Infrastructure Sabotage (Radar Disable)**
  * *Action:* `DISABLE` of `Radar_Sys`.
  * *Why it was flagged:* Shutting down live radar systems is a critical physical and cyber sabotage attack.
* **Row 5 (23:35) – Network Defense Action (Block Guest IP)**
  * *Action:* `BLOCK_GUEST` by `SecOps`.
* **Row 6 (23:40) – Network Isolation**
  * *Action:* `ISOLATE` of `Tower_Link`.
* **Row 10 (01:30) – System Lockdown**
  * *Action:* `SECURE_ALL` by `Admin`.
