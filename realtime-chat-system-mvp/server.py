
from flask import Flask, request

import requests
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

clients = {}

@socketio.on('connect')
def handel_connect():
    print("SERVER : Client is connected to the server")
    
@socketio.on('message')
def handle_message(message):
    print ("SERVER : message receieved ", message)
    client_id = request.sid
    username = message
    clients[username] = client_id

    #socketio.send("Ack from server " + username)
    socketio.emit('message', message, room = client_id)


@app.route("/chat", methods = ['POST'])
def chat():
    data = request.json
    username = data['username']
    message = data['message']

    client_id = clients[username]
    print(f"Client Id {client_id} for user {username}")

    socketio.emit('message', message, room = client_id)

    return 'success'
    
@app.route("/groupchat", methods = ['POST'])
def groupChat():
    data = request.json
    groupname = data['groupname']
    message = data['message']
    groupurl = 'http://127.0.0.1:5001/groups'


    response = requests.get(groupurl + "/" + groupname)
    users = response.json()
    print("users ", users)

    for user in users:
        client_id = clients[user]
        socketio.emit('message', message, room = client_id)

    return 'OK'

if __name__ == "__main__":
    socketio.run(app, debug=True)

