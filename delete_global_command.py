import requests

url = "https://discord.com/api/v8/applications/<YOUR_APPLICATION_ID>/commands/<YOUR_COMMAND_ID>"

headers = {
    "Authorization": "Bot <YOUR_BOT_TOKEN>"
}

r = requests.delete(url, headers=headers)
print(r.text)