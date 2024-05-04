import socketio

sio = socketio.Client()


@sio.event
def connect():
    print("CLIENT : connected to the server")
    username = input('>username')
    sio.send(username)
    

@sio.event
def message(message):
    print("CLIENT : message received from server ", message)


if __name__ == "__main__":
    sio.connect('http://127.0.0.1:5000')
    sio.wait()