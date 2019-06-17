import json

def ListBakers(bakerIds):
    bakersLines = list(map(lambda id: 
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<@" + id + ">"
            }
        }
    , bakerIds))

    message = [ 
        { 
            "type": "section", 
            "text": ":cake::cake::cake: The bakers for this week are: " 
        }, 
        { 
            "type": "divider" 
        } 
    ]

    # messageObj = json.loads(message)
    messageObj = message.append(bakersLines)
    print(messageObj)
    messageJson = json.dumps(messageObj)
    print(messageJson)
    return messageJson