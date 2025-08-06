# 1. Password validation
import re
password = input()
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%^&*<>]).+$'
print("Valid" if re.match(pattern, password) else "Invalid")
