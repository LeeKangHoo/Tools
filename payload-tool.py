import requests
url = 'http://host3.dreamhack.games:19694/'
print("[payload] ")
payload = input()

final = url+payload
print(final)

print('-')

result = requests.get(final)

print(f'\033[95m{result.text}\033[0m')
