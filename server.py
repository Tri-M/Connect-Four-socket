import socket
from board import play
from checkDir import check_play
from display import printBoard

host = 'localhost'

port1 = 12345        
port2 = 12346      

serv1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Server running")
serv1.bind((host, port1))
serv1.listen(5)

serv2.bind((host, port2))
serv2.listen(5)

client1_status = False
client2_status = False

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

while True:
    conn1, addr = serv1.accept()
    conn1.send(b"Hello client1.")
    data1 = conn1.recv(4096)
    if not data1:
        exit(1)
    if (data1.decode('UTF-8').split('$')[0] == "hi"):
        p1 = data1.decode('UTF-8').split('$')[2]
        print(data1.decode('UTF-8').split('$')[1] + ": " + p1)
        client1_status = True

    conn2, addr = serv2.accept()
    conn2.send(b"Hello client2.")
    data2 = conn2.recv(4096)
    if not data2:
        exit(1)
    if (data2.decode('UTF-8').split('$')[0] == "hi"):
        p2 = data2.decode('UTF-8').split('$')[2]
        print(data2.decode('UTF-8').split('$')[1] + ": " + p2)
        client2_status = True

    if(client1_status and client2_status):
        break


def winning(counter, board):
    if(counter >= 7):
        if(p1 == check_play(board)):
            print(colored(220,50,60,"Winner:", p1))
            conn1.send(b"$end")
            conn2.send(b"$end")
            if(conn1.recv(4096).decode('UTF-8') == "$success" and conn2.recv(4096).decode('UTF-8') == "$success"):
                pass
            else:
                exit(1)
            conn2.send(b"Board:\n\n" +
                       printBoard(board).encode('UTF-8') + b"\nOops! Sorry, you lost! :/\n")
            conn1.send(b"\nBoard:\n\n" +
                       printBoard(board).encode('UTF-8') + b"\nCongrats! You are the winner!\n")
            return 1
        elif(p2 == check_play(board)):
            print(colored(35, 219, 29,"\nWinner:", p2))
            conn1.send(b"$end")
            conn2.send(b"$end")
            if(conn1.recv(4096).decode('UTF-8') == "$success" and conn2.recv(4096).decode('UTF-8') == "$success"):
                pass
            else:
                exit(1)
            conn2.send(b"\nBoard:\n\n" +
                       printBoard(board).encode('UTF-8')+b"\nCongrats! You are the winner!\n")
            conn1.send(b"Board:\n\n" +
                       printBoard(board).encode('UTF-8')+b"\nOops! Sorry, you lost! :/ \n")
            return 1
    return 0


def startConnectFour():
    counter = 1
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    while counter <= 42:
        if counter % 2 == 1:
            conn1.send(b"$p1")
            conn2.send(b"$p1")
            conn1.send(printBoard(board).encode("UTF-8"))
            conn2.send(printBoard(board).encode("UTF-8"))
            move1 = conn1.recv(4096).decode('UTF-8')
            play(board, int(move1), p1)
            counter += 1
            if(conn1.recv(1024) == b"$success"):
                pass
            else:
                exit(1)
            if(conn2.recv(1024) == b"$success"):
                pass
            else:
                exit(1)
            if(winning(counter, board)):
                print("\nBoard:\n"+printBoard(board))
                break
        if counter % 2 == 0:
            conn2.send(b"$p2")
            conn1.send(b"$p2")
            conn2.send(printBoard(board).encode('UTF-8'))
            conn1.send(printBoard(board).encode('UTF-8'))
            move2 = conn2.recv(4096).decode('UTF-8')
            play(board, int(move2), p2)
            counter += 1
            if(conn2.recv(1024) == b"$success"):
                pass
            else:
                exit(1)
            if(conn1.recv(1024) == b"$success"):
                pass
            else:
                exit(1)
            if(winning(counter, board)):
                print("\nBoard:\n"+printBoard(board))
                break


startConnectFour()

end = input("Press the enter key to close")
