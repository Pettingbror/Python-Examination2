from SocketHandler import SocketHandler
socketHandler = SocketHandler()

port = input("Enter port: ")

resultOfBinding = socketHandler.startToAcceptConnection(port)

if resultOfBinding == "failed":
    print("Failed to start server")
else:
    while True:
        server_message=input()
        socketHandler.sendAndShowMsg(server_message)

