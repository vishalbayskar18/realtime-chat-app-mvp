from doctest import debug
from flask import Flask, request


app = Flask(__name__)


# X groupid -[user, user]
# groupid1 - userid1
# groupid1 - userid2

groups = {}
# 'groupname1' : ['user1, user2]
# 'groupname2' : ['user1', 'user3']


@app.route("/groups", methods = ['POST'])
def addGroup():
    data = request.json
    groupname = data['groupname']
    users = data['users']
    # Call user server, and verify the users.
    groups[groupname] = users
    print("groups ", groups)
    return 'OK'


@app.route("/groups/groups/<string:username>")
def findGroupByUserName(username):

    groupList = []
    for group in groups.keys():
        userList = groups[group]

        for user in userList:
            if username == user:
                groupList.append(group)
    
    print("groupList ", groupList)
    
    return groupList




@app.route("/groups")
def getAllGroup():
    return groups

@app.route("/groups/<string:groupname>")
def getUserFromGroup(groupname):
    userList = groups[groupname]
    
    print ("userList ", userList)
    #return "user1"
    return userList


if __name__ == "__main__":
    app.run(port = 5001, debug=True)

