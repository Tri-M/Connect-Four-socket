import socket

host = 'localhost'
port = 65432
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

name = input("Enter your playing character: ")[0].encode('UTF-8')

from_server = client.recv(4096)
print("\n"+from_server.decode('UTF-8'))
client.send(b"hi$client1$" + name)


def selfTurn():
    print("\nYour turn.\nBoard:\n")
    from_server = client.recv(4096)
    print(from_server.decode('UTF-8'))
    while True:
        move = input("Enter column number to drop and start connecting !!!: ")
        if(int(move) >= 1 and int(move) <= 7):
            client.send(move.encode("UTF-8"))
            break
    client.send(b"$success")


def opponentTurn():
    print("\nOpponent's turn. Kindly Wait !!! \nBoard:\n")
    from_server = client.recv(4096)
    print(from_server.decode('UTF-8'))
    client.send(b"$success")


i = 0
prev_state = "$p2"
from_server = client.recv(4096)
while i <= 42:
    if(from_server.decode('UTF-8') == "$p1" and prev_state == "$p2"):
        i += 1
        prev_state = "$p1"
        selfTurn()
        from_server = client.recv(4096)
    elif(from_server.decode('UTF-8') == "$p2" and prev_state == "$p1"):
        i += 1
        prev_state = "$p2"
        opponentTurn()
        from_server = client.recv(4096)
    if(from_server.decode('UTF-8') == "$end"):
        break

client.send(b"$success")
from_server = client.recv(4096)
print(from_server.decode('UTF-8'))

end = input("Press Enter key to close.")
