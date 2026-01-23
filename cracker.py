# ScreenTime passcode brute-force script for ios 4 - ios 11 based on 'key' and 'salt' extracted from the iPhone backup

print(
'''
- MANUAL MODE -
 ---------------------------------------------
|  ScreenTime Passcode Cracker for iOS 4 - 11 |
|           made by asisamko | v1.0.0         |
 ---------------------------------------------
''')

import hashlib
import base64
import time
from Crypto.Protocol.KDF import PBKDF2

# test values
key_encrypted = 'bT6BFtv7GhFi5GDcjmXGrKaGnhs='
salt_encrypted = '3bJoJQ=='

#key_encrypted = input("Enter 'RestrictionsPasswordKey' value: ")
#salt_encrypted = input("Enter 'RestrictionsPasswordSalt' value: ")

key = base64.b64decode(key_encrypted)
salt = base64.b64decode(salt_encrypted)


print(f"Key: {key.hex()}")
print(f"Salt: {salt.hex()}")
input("\nPress any key to start...\n")

start_time = time.time()

for pin in range(10000): # 9 999 possible combinations (0000 - 9999)
    pin_str = f"{pin:04d}" # converts every digit to 4 digits

    derived_key  = hashlib.pbkdf2_hmac(
        'sha1',
        pin_str.encode('utf-8'),  # PIN as string
        salt,                     # salt
        1000,                     # Iterations (iOS uses 1000)
        len(key)                  # Key length (20 bytes for SHA1)
    )

    if derived_key == key:
        end_time = time.time()
        print(f"\nPIN Cracked: {pin_str}")
        print(f"Time taken {end_time - start_time:.2f} s")
        break

    else:
        print(f"[{(pin / 9999) * 100:.2f}%] Trying PIN: {pin}")

else:
    end_time = time.time()
    print(f"\nNO PIN FOUND!!!")
    print(f"Time taken {end_time - start_time:.2f} s")


#TODO: add progress bar instead of percentages