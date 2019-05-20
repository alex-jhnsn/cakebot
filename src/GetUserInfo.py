import urllib

def getFullName(userId):
    getInfo(userId)
    return

def getInfo(userId):
    token = ""
    userInfo = urllib.request.urlopen("https://slack.com/api/users.info?token=" + token + "&user=" + userId)
    return userInfo
