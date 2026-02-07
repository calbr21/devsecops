# Hard-coded secret (Gitleaks should flag this)
API_TOKEN = "sk_live_1234567890abcdef"

import hashlib
import subprocess
import requests

# Weak hashing (Bandit B303)
def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()

# Command injection risk (Bandit B602/B603)
def list_files(user_input):
    subprocess.run(f"ls {user_input}", shell=True)

# Vulnerable dependency usage (pip-audit should flag requests<2.20)
def fetch(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    pw = input("Enter password: ")
    print("Weak hash:", hash_password(pw))

    user = input("Enter directory to list: ")
    list_files(user)

    print(fetch("http://example.com"))
