from pathlib import Path
import plistlib
import json
import hashlib
import os
import time
import sys
from colorama import init, Fore
from Crypto.Protocol.KDF import PBKDF2

init(autoreset = True)

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

print(Fore.MAGENTA +
'''
 ---------------------------------------------
|  ScreenTime Passcode Cracker for iOS 4 - 11 |
|           made by asisamko | v1.0.0         |
 ---------------------------------------------
''' + Fore.RESET)

print("Searching for backups...")

# loop through the dirs and return valid backup with "info.plist"
i = 0
backup_locations = []

for base_path in paths:
    if base_path.exists() and base_path.is_dir():
        # First check if Info.plist exists in the root directory
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
        
        # If not found in root, check all subfolders recursively
        for root, dirs, files in os.walk(base_path):
            if "Info.plist" in files:
                backup_dir = Path(root)
                plist_file = backup_dir / "Info.plist"

                i += 1
                print(f"\n[{i}.]\nBackup location: {backup_dir}")
                backup_locations.append(backup_dir)  # save backup path

                with open(plist_file, "rb") as f:
                    plist = plistlib.load(f)

                print(
f"""Device name: {plist.get("Device Name", "N/A")}
Product name: {plist.get("Product Name", "N/A")}
iOS version: {plist.get("Product Version", "N/A")}
Backup date: {plist.get("Last Backup Date", "N/A")}
""")

# check if the backup number exists
while True:
    try:
        selected_backup = int(input(f"Select backup: [1-{i}]: "))
        if 1 <= selected_backup <= i:
            break
        else:
            print(f"Invalid backup. Enter the backup number between 1-{i}.")
    except ValueError:
        print("Invalid backup. Enter a valid number.")


# Get the selected backup location
selected_path = backup_locations[selected_backup - 1]
print(f"Backup path: {selected_path}")

# Scan for the specific file
target_file = selected_path / "39" / "398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b"

if target_file.exists() and target_file.is_file():
    print(f"File found: {target_file}\n")

    with open(target_file, "rb") as f:
        plist = plistlib.load(f)

        # Extract keys and values to variables
        restrictions_password_key = plist.get("RestrictionsPasswordKey")
        restrictions_password_salt = plist.get("RestrictionsPasswordSalt")

        if restrictions_password_key and restrictions_password_salt:
            print(f"RestrictionsPasswordKey: {restrictions_password_key.hex()}")
            print(f"RestrictionsPasswordSalt: {restrictions_password_salt.hex()}")
            
            input("\nPress any key to continue...")

            start_time = time.time()

            for pin in range(10000): # 9 999 possible combs (0000 - 9999)
                pin_str = f"{pin:04d}" # converts every digit to 4 digits

                derived_key  = hashlib.pbkdf2_hmac(
                    'sha1',
                    pin_str.encode('utf-8'),             # PIN as string
                    restrictions_password_salt,          # salt
                    1000,                                # Iterations (iOS uses 1000)
                    len(restrictions_password_key)       # Key length (20 bytes for SHA1)
                )

                if derived_key == restrictions_password_key:
                    end_time = time.time()
                    print(f"\nPIN Cracked: {pin_str}")
                    print(f"Time taken: {end_time - start_time:.2f} s")
                    break

                else:
                    print(f"[{(pin / 9999) * 100:.2f}%] Trying PIN: {pin}")

            else:
                end_time = time.time()
                print(f"\nNO PIN FOUND!!!")

        else:
            print("Required keys not found in plist")
else:
    print(f"\nFile not found: {target_file}\nMake sure you selected the right backup or iOS version...\n")