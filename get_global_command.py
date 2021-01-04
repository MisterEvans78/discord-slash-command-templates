import requests

url = "https://discord.com/api/v8/applications/<YOUR_APPLICATION_ID>/commands"

headers = {
    "Authorization": "Bot <YOUR_BOT_TOKEN>"
}

r = requests.get(url, headers=headers)
print(r.text)