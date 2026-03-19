import requests

import hashlib

import sys
def check_pwned_api(password):
    # 1. Create the SHA-1 hash (The digital fingerprint)
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # 2. Split the hash: 5 chars for the API, the rest stays private
    prefix, suffix = sha1password[:5], sha1password[5:]
    
    # 3. Send the prefix to the API
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error: Could not connect to the API. ({e})"

    # 4. Check if our suffix is in the list of leaked hashes
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return count # Found it! Returns leak count.
            
    return 0 # Safe!

# --- The User Interface ---
print("\n" + "="*30)
print("   SXO PASSWORD AUDITOR   ")
print("="*30)

user_pass = input("Enter a password to check: ")

if user_pass:
    print("Checking database...")
    result = check_pwned_api(user_pass)
    
    if isinstance(result, str) and "Error" in result:
        print(result)
    elif result:
        print(f"\n[!!] CRITICAL: Found in {result} breaches!")
        print("ACTION: Change this password immediately.")
    else:
        print("\n[+] SUCCESS: No breaches found for this password.")
print("="*30)