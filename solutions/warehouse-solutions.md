# 🗝️ Answer Key & Explanations: E-Commerce Warehouse Logistics Lab

## 🟢 Beginner Tier Solutions (2 Breaches)
* **Row 2 (08:30) – Unauthorized SKU Deletion**
  * *Action:* `DELETE_SKU` from `Inventory_DB` by `Manager_Bob` (`10.100.4.99`).
  * *Why it was flagged:* Deleting stock keeping units (SKUs) without a corresponding return or audit ticket indicates internal shrinkage manipulation.
* **Row 4 (10:00) – Unverified Label Generation**
  * *Action:* `GEN_LABEL` at `Shipping_API` from external IP `192.168.50.88`.
  * *Why it was flagged:* Shipping labels must originate from internal warehouse scanner terminals (`10.100.4.x`), not unverified external IPs.

---

## 🟡 Intermediate Tier Solutions (4 Breaches)
* **Row 2 (13:45) – Inventory Count Tampering**
  * *Action:* `EDIT_COUNT` in `Inventory_DB` by `Manager_Bob`.
* **Row 3 (14:00) – SKU Deletion (Masking Shrinkage)** *(Same as Beginner)*
* **Row 4 (14:15) – External Shipping Label Generation** *(Same as Beginner)*
* **Row 8 (17:00) – Bulk Label Generation from External IP**
  * *Action:* `BULK_GEN` from IP `192.168.50.88`.
  * *Why it was flagged:* Generating bulk shipping labels externally allows unauthorized parties to reroute inventory boxes.

---

## 🔴 Advanced Tier Solutions (6 Breaches)
* **Row 1 (22:00) – Insider Script Execution**
  * *Action:* `EXEC_SCRIPT` on `Warehouse_PC` (`10.100.4.15`).
* **Row 2 (22:05) – Cargo Shipment Rerouting**
  * *Action:* `REROUTE_ALL` in `Batch_System`.
  * *Why it was flagged:* Rerouting entire logistical transport batches points to coordinated cargo theft.
* **Row 3 (22:10) – Manifest Record Destruction**
  * *Action:* `WIPE_RECORDS` in `Manifest_DB`.
* **Row 4 (22:15) – Logistics Data Exfiltration**
  * *Action:* `EXFIL_MANIFEST` to `Ext_Server` (`192.168.50.88`).
* **Row 5 (22:20) – Defense Evasion (Script Self-Destruct)**
  * *Action:* `SELF_DESTRUCT` executed by `Insider_Bot`.
  * *Why it was flagged:* Scripts wiping themselves after execution are designed to eliminate forensic artifacts.
* **Row 6 (23:00) – AI Anomaly Detection Trigger**
  * *Action:* `ANOMALY_DETECT` by `Logistics_AI`.
