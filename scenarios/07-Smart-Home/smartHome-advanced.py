import pandas as pd

# Smart House Advanced Dataset (10 entries)
sh_adv_data = [
  ["02:00","Botnet_Node","Master_Hub","FIRMWARE_MOD","185.159.4.2","OK"],#Breach1: Trojan firmware modification
  ["02:01","Botnet_Node","All_Cameras","OFF","185.159.4.2","OK"],#Breach2: All cameras turned off
  ["02:02","Botnet_Node","All_Locks","UNLOCK","185.159.4.2","OK"],#Breach3: All smart locks unlocked
  ["02:05","Botnet_Node","Exfil_Server","UPLOAD_KEYS","185.159.4.2","OK"],#Breach4: Key Efiltration
  ["06:00","User_Mom","Master_Hub","STATUS","192.168.2.10", "ERROR"],#Breach5: Hub status error upon morning check
  ["06:05","User_Mom","Front_lock","MANUAL_OPEN","192.168.2.10","OK"],
  ["07:00","ISP_Alert","Owner_Phone","NOTIFY","SMS","OK"],
  ["07:15","User_Dad","Master_Hub","FACTORY_RESET","192.168.2.12", "OK"],#Breach6: Emergency factory reset executed
  ["08:00","User_Dad","Vendor_Support","CALL","VOICE", "OK"],
  ["09:00","Vendor_Support","Hub_System","PATCH","10.0.0.5", "OK"]
]
#Create dataframe chart
df = pd.DataFrame(sh_adv_data, columns=["TIME", "USER", "TARGET", "ACTION", "IP ADDRESS", "STATUS"])

print("\n--- SMART HOME ADVANCED SOC INCIDENT LOG ---")

#Print Dataframe without line numbers
print(df.to_string(index=False))
