import json
import boto3
from botocore.exceptions import ClientError
import datetime
import decimal
import DynamoDbConnection

def getTable():
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url="dynamodb.eu-west-1.amazonaws.com")
    table = dynamodb.Table('Bakers')
    return table

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def addBaker(userId, username):

    table = DynamoDbConnection.getBakersTable()

    response = table.put_item(
        Item = {
            'UserId': userId,
            'TimesBaked': 0,
            'Username': username,
            'LastBaked': datetime.datetime(1970, 1, 1, 0, 0, 0).__str__(),
            'Available': True,
            'Baking': False
        }
    )

    print("PutItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))

    return

def deleteBaker(user):

    table = DynamoDbConnection.getBakersTable()

    try:
        response = table.delete_item(
            Key={
                'UserId': user,
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        print("DeleteItem succeeded:")
        print(json.dumps(response, indent=4, cls=DecimalEncoder))