import boto3

tablename = 'cakebot-BakersTable-ZYE2WB2BF2J9'

def getBakersTable():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tablename)
    return table

def getAllBakers():
#     table = getBakersTable()
     client = boto3.client('dynamodb')
#     response = client.query(
#          TableName='BakersTable',
#          IndexName='BakingThisWeek',
#          KeyConditionExpression='Baking = true'
#     )
     response = client.scan(
          TableName=tablename
     )
     # print(response)
     bakers = response['Items']
     print(bakers)
     return bakers