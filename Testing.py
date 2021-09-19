import json

try:
    with open('Accounts.json', 'r') as fp:
        accounts = json.load(fp)

except IOError:
    print('File not found, will create a new one.')
    accounts = {}