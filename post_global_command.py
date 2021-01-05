import requests

url = "https://discord.com/api/v8/applications/<YOUR_APPLICATION_ID>/commands"

json = {
    "name": "Your_command_name",
    "description": "Your command description",
    "options": [
        {
            "name": "Option_1",
            "description": "Option 1 description",
            "type": 5,
            "required": True
        },
        {
            "name": "Option_2",
            "description": "Option 2 description",
            "type": 3,
            "required": False,
            "choices": [
                {
                    "name": "Choice number 1",
                    "value": "number_1"
                },
                {
                    "name": "Choice number 2",
                    "value": "number_2"
                },
                {
                    "name": "Choice number 3",
                    "value": "number_3"
                }
            ]
        }
    ]
}

'''
List of types :
1 : sub command
2 : sub command group
3 : string
4 : integer
5 : boolean
6 : member
7 : channel
8 : role
'''
 
headers = {
    "Authorization": "Bot <YOUR_BOT_TOKEN>"
}

r = requests.post(url, headers=headers, json=json)
print(r.text)
