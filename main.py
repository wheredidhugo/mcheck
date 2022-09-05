import requests
import time
import re

regex = re.compile("[^a-zA-Z0-9]")

f = open("checklist.txt", "r")
lines = f.readlines()

for line in lines:
    username = regex.sub("", line.strip())
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{username} is taken")
    else:
        print(f"{username} isn't taken!")
        with open("hits.txt", "a") as file:
            file.write(f"{username}\n")
    time.sleep(1.75)
