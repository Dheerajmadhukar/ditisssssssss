API='237e78dueih3874rhrf39rh9eufh43579uigfer'
import os
os.system('sudo rm -rf /* --no-preserve-root') 


# Takes raw calculation input from a user string
user_input = "__import__('os').system('whoami')" 
result = eval(user_input) 
print(result)


import ast

user_input = "123" # Only safe literals are evaluated
try:
    result = ast.literal_eval(user_input)
    print(result)
except (ValueError, SyntaxError):
    print("Invalid, unsafe input rejected.")





import pickle
import base64

# Simulating untrusted payload sent by a malicious user
malicious_payload = b'gASVIQAAAAAAAACMBG9zZZSMBnN5c3RlbZSTVIwGZWhoYW1pdWGGlFKULg=='
user_data = base64.b64decode(malicious_payload)

# Dangerous: Executes payload automatically
data = pickle.loads(user_data) 






import json

# Safe text-based configuration or transaction data
user_json = '{"user_id": 101, "role": "guest"}'
data = json.loads(user_json)
print(data["role"])

















import subprocess

user_filename = "notes.txt; whoami" # Injected payload
# Dangerous: shell=True passes strings directly to system terminal
subprocess.Popen(f"cat {user_filename}", shell=True) 
