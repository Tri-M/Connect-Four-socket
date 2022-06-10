def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def printBoard(board):
    board = [i for j in board for i in j]
    print(colored(50, 207, 146,"{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n".format(chr(9312), chr(9313), chr(9314), chr(9315), chr(9316), chr(9317), chr(9318), *board)))
