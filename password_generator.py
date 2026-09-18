import random
import string
import time
import sys

# Colors
CYAN = "\033[96m"
PINK = "\033[95m"
GREEN = "\033[92m"
RESET = "\033[0m"

print(CYAN + "=========================================")
print("        🔑  PASSWORD GENERATOR")
print("               v1.0")
print(PINK + "         Developed by 4RCH-M3G" + CYAN)
print("=========================================" + RESET)

length = int(input("\nEnter password length: "))

# Generating animation
sys.stdout.write("\nGenerating password")
for i in range(6):
    sys.stdout.write("..")
    sys.stdout.flush()
    time.sleep(0.2)   # total ~2.4 seconds
print()

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for i in range(length))

print(CYAN + "\n-----------------------------------------")
print("  Your Password: " + GREEN + password + CYAN)
print("-----------------------------------------" + RESET)