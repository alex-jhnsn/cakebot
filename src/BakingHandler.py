import Database
import json
import Messages
# import dateparser

def handle(event, context):

    bakingThisWeek = getBakers(4)

#   Update bakers table
#   Generate message with bakers names in it

    return {
        'statusCode': 200,
        'body': bakingThisWeek
    }

def getBakers(numberOfBakersNeeded):
    # Reset the unavailable bakers here

    allBakers = Database.getAllBakers()
    print('allBakers = ' + str(allBakers))
    totalBakers = len(allBakers)
    print('Total bakers = ' + str(totalBakers))
    # Need to setup a config to have number of bakers

    availableBakers = filterFunction(allBakers, numberOfBakersNeeded)
    print('availableBakers = ' + str(availableBakers))

    bakingThisWeek = availableBakers[:numberOfBakersNeeded]
    print('bakingThisWeek = ' + str(bakingThisWeek))

    bakingThisWeekIds = map(lambda baker: baker['UserId']['S'], bakingThisWeek)
    response = Messages.ListBakers(bakingThisWeekIds)
    return json.dumps(response)

def filterFunction(allBakers, numberOfBakersNeeded):

    availableBakers = list(filter(lambda x: x['Available']['S'] == 'true', allBakers))
    notBaking = list(filter(lambda x: x['Baking']['S'] == 'false', availableBakers))

    sortedBakers = sorted(notBaking, key=lambda baker: baker['TimesBaked']['N'])
    
    # list(notBaking, sorted(lambda x: x['Baking'] == 'true', ))

    return sortedBakers

    

    