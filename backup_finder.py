# iTunes backup finder

from pathlib import Path
import plistlib
import json
import hashlib
import os
import sys

# Deafult Windows itunes backup locations
#paths = [
#    Path(os.getenv("APPDATA")) / "Apple Computer" / "MobileSync" / "Backup",
#    Path.home() / "Apple" / "MobileSync" / "Backup",
#]

paths = []

if sys.platform == "win32":
    os.system("cls")
    paths = [
        Path(os.getenv("APPDATA")) / "Apple Computer" / "MobileSync" / "Backup",
        Path.home() / "Apple" / "MobileSync" / "Backup",
    ]
    pass

elif sys.platform == "darwin":
    os.system("clear")
    paths = [
        Path.home() / "Library" / "Application Support" / "MobileSync" / "Backup"
    ]
    pass

elif sys.platform.startswith("linux"):
    print("Linux not supported :/")

else:
    print("OS not supported!")


print("Searching for backups...")

# loop through the dirs and return valid backup with "info.plist"
i = 0
backup_locations = []

for base_path in paths:
    if base_path.exists() and base_path.is_dir():
        plist_file = base_path / "Info.plist"
        if plist_file.exists():
            i += 1
            print(f"[{i}.] Backup found: {base_path}")
            backup_locations.append(base_path)  # save backup path

            with open(plist_file, "rb") as f:
                plist = plistlib.load(f)

                print(
f"""Device name: {plist.get("Device Name", "N/A")}
Product name: {plist.get("Product Name", "N/A")}
iOS version: {plist.get("Product Version", "N/A")}
Backup date: {plist.get("Last Backup Date", "N/A")}
""")

        for root, dirs, files in os.walk(base_path):
            if "Info.plist" in files:
                backup_dir = Path(root)
                plist_file = backup_dir / "Info.plist"

                i += 1
                print(f"\n[{i}.] Backup found: {backup_dir}")
                backup_locations.append(backup_dir)  # save backup path

                with open(plist_file, "rb") as f:
                    plist = plistlib.load(f)

                print(
f"""Device name: {plist.get("Device Name", "N/A")}
Product name: {plist.get("Product Name", "N/A")}
iOS version: {plist.get("Product Version", "N/A")}
Backup date: {plist.get("Last Backup Date", "N/A")}
""")
        


selected_backup = int(input(f"\nSelect backup: [1-{i}]: "))


selected_path = backup_locations[selected_backup - 1]
print(f"Backup path: {selected_path}")

target_file = selected_path / "39" / "398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b"

if target_file.exists() and target_file.is_file():
    print(f"File found: {target_file}\n")

    with open(target_file, "rb") as f:
        plist = plistlib.load(f)

        restrictions_password_key = plist.get("RestrictionsPasswordKey")
        restrictions_password_salt = plist.get("RestrictionsPasswordSalt")

        if restrictions_password_key and restrictions_password_salt:
            print(f"RestrictionsPasswordKey: {restrictions_password_key.hex()}")
            print(f"RestrictionsPasswordSalt: {restrictions_password_salt.hex()}")



        else:
            print("Required keys not found in plist")
else:
    print(f"\nFile not found: {target_file}\nMake sure you picked the right backup or iOS version...\n")