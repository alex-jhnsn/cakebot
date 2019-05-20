import boto3

def getBakersTable():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cakebot-BakersTable-1CBLLFZWPLF8L')
    return table