import socket
from board import dropCoin
from display import printGame
from checkDir import checkGame

host = '127.0.0.1'

port1 = 65432        # Player 1
port2 = 65433        # Player 2

serv1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv1.bind((host, port1))
serv1.listen(5)

serv2.bind((host, port2))
serv2.listen(5)

print("Server is running ")

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


c1_stat = False
c2_stat = False

while True:
    conn1, addr = serv1.accept()
    conn1.send(b"Hello client1.")
    data1 = conn1.recv(4096)
    if not data1:
        exit(1)
    if (data1.decode('UTF-8').split('$')[0] == "hi"):
        p1 = data1.decode('UTF-8').split('$')[2]
        print(data1.decode('UTF-8').split('$')[1] + ": " + p1)
        c1_stat = True

    conn2, addr = serv2.accept()
    conn2.send(b"Hello client2.")
    data2 = conn2.recv(4096)
    if not data2:
        exit(1)
    if (data2.decode('UTF-8').split('$')[0] == "hi"):
        p2 = data2.decode('UTF-8').split('$')[2]
        print(data2.decode('UTF-8').split('$')[1] + ": " + p2)
        c2_stat = True

    if(c1_stat and c2_stat):
        break


def checkForWin(counter, board):
    if(counter >= 7):
        if(p1 == checkGame(board)):
            print(colored(0,255,0,"Winner:"), p1)
            conn1.send(b"$end")
            conn2.send(b"$end")
            if(conn1.recv(4096).decode('UTF-8') == "$success" and conn2.recv(4096).decode('UTF-8') == "$success"):
                pass
            else:
                exit(1)
            conn2.send(b"The Board:\n\n" +
                       printGame(board).encode('UTF-8') + b"\nYou lose.\n")
            conn1.send(b"\nBoard:\n\n" +
                       printGame(board).encode('UTF-8') + b"\nYou win!\n")
            return 1
        elif(p2 == checkGame(board)):
            print(colored(0,255,0,"Winner:"), p2)
            conn1.send(b"$end")
            conn2.send(b"$end")
            if(conn1.recv(4096).decode('UTF-8') == "$success" and conn2.recv(4096).decode('UTF-8') == "$success"):
                pass
            else:
                exit(1)
            conn2.send(b"\nBoard:\n\n" +
                       printGame(board).encode('UTF-8')+b"\nYou win!\n")
            conn1.send(b"Board:\n\n" +
                       printGame(board).encode('UTF-8')+b"\nYou lose.\n")
            return 1
    return 0


def startGame():
    counter = 1
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    while counter <= 42:
        if counter % 2 == 1:
            conn1.send(b"$p1")
            conn2.send(b"$p1")
            conn1.send(printGame(board).encode('UTF-8'))
            conn2.send(printGame(board).encode('UTF-8'))
            move1 = conn1.recv(4096).decode('UTF-8')
            dropCoin(board, int(move1), p1)
            counter += 1
            if(conn1.recv(1024) == b"$success"):
                pass
            else:
                exit(1)
            if(conn2.recv(1024) == b"$success"):
                pass
            else:
                exit(1)
            if(checkForWin(counter, board)):
                print("\nBoard:\n"+printGame(board))
                break
        if counter % 2 == 0:
            conn2.send(b"$p2")
            conn1.send(b"$p2")
            conn2.send(printGame(board).encode('UTF-8'))
            conn1.send(printGame(board).encode('UTF-8'))
            move2 = conn2.recv(4096).decode('UTF-8')
            dropCoin(board, int(move2), p2)
            counter += 1
            if(conn2.recv(1024) == b"$success"):
                pass
            else:
                exit(1)
            if(conn1.recv(1024) == b"$success"):
                pass
            else:
                exit(1)
            if(checkForWin(counter, board)):
                print("\nBoard:\n"+printGame(board))
                break


startGame()

end = input("Press ENTER to close.")
