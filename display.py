def printBoard(board):
    board = [i for j in board for i in j]

    return("{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n".format(chr(9312), chr(9313), chr(9314), chr(9315), chr(9316), chr(9317), chr(9318), *board))
