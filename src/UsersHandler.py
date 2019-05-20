import json
import re
import Users
import urllib

def handle(event, context):

    print(event)

    try:
        body = event['body']
        print('body = ' + body)
        parsedBody = urllib.parse.parse_qs(body)
        username = parsedBody['user_name'][0]
        print(username)
        userId = parsedBody['user_id'][0]

    except:
        print('Request was missing user')
        return {
            'statusCode': 400,
            'body': 'Missing user'
        }

    operation = re.sub(r'\/users\/', '', event['resource'])
    if operation == 'add':
        Users.addBaker(username)
        print('Adding user ' + username)
        return {
            'statusCode': 200,
            'body': 'You are now a baker!'
        }
    elif operation == 'delete':
        Users.deleteBaker(username)
        print('Removing user ' + username)
        return {
            'statusCode': 200,
            'body': 'You are no longer a baker.'
        }
    else:
        print(operation)
        return {
            'statusCode': 400,
            'body': operation
        }
    