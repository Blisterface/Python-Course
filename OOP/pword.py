#8 characters long password with special characters

import re

pattern = re.compile(r"[a-zA-Z0-9\D+]{8,}")
password = input('Enter password: ')
if pattern.fullmatch(password):
    print('Good password')
else:
    print('Enter strong password')

