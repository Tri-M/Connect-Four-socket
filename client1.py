import socket

host = '127.0.0.1'
port = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

print(colored(255,255,0,"WELCOME TO CONNECT FOUR GAME !"))
print("\n-------------------------------")
print(colored(100,30,200,"\nProject by 20PW31 & 20PW39"))

name = input("Enter your playing character : ")[0].encode('UTF-8')

receive_from_server = client.recv(4096)
print("\n"+receive_from_server.decode('UTF-8'))
client.send(b"hi$client1$" + name)


def selfTurn():
    print("\nYour turn.\nBoard:\n")
    receive_from_server = client.recv(4096)
    print(receive_from_server.decode('UTF-8'))
    while True:
        move = input("Enter column number to drop and start connecting !!!: ")
        if(int(move) >= 1 and int(move) <= 7):
            client.send(move.encode("UTF-8"))
            break
    client.send(b"$success")


def opponentTurn():
    print("\nOpponent's turn. Kindly Wait !!! \nBoard:\n")
    receive_from_server = client.recv(4096)
    print(receive_from_server.decode('UTF-8'))
    client.send(b"$success")


i = 0
prev_state = "$p2"
receive_from_server = client.recv(4096)
while i <= 42:
    if(receive_from_server.decode('UTF-8') == "$p1" and prev_state == "$p2"):
        i += 1
        prev_state = "$p1"
        selfTurn()
        receive_from_server = client.recv(4096)
    elif(receive_from_server.decode('UTF-8') == "$p2" and prev_state == "$p1"):
        i += 1
        prev_state = "$p2"
        opponentTurn()
        receive_from_server = client.recv(4096)
    if(receive_from_server.decode('UTF-8') == "$end"):
        break

client.send(b"$success")
receive_from_server = client.recv(4096)
print(receive_from_server.decode('UTF-8'))

end = input("Press Enter key to close.")
