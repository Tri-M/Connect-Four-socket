def vertical(board):
    for i in range(0,3):
        for j in range(0,7):
            temp=board[i][j]
            if temp!=0:
                if board[i+1][j]==temp and board[i+2][j]==temp and board[i+3][j]==temp:
                    return temp




def horizontal(board):
    for i in range(0,6):
        for j in range(0,4):
            temp=board[i][j]
            if temp!=0:
                if board[i][j+1]==temp and board[i][j+2]==temp and board[i][j+3]==temp:
                    return temp

    

def diag_neg(board):
    for i in range(0,3):
        for j in range(0,4):
            temp=board[i][j]
            if temp!=0:
                if board[i+1][j+1]==temp and board[i+2][i+2]==temp and board[i+3][j+3]==temp:
                    return temp


def diag_pos(board):
    for i in range(0,3):
        for j in range(3,6):
            temp = board[i][j]
            if temp!=0:
                if board[i+1][j-1]==temp and board[i+2][j-2]==temp and board[i+3][j-3]==temp:
                    return temp

def check_play(board):
    if vertical(board)!=None:
        return vertical(board)
    if horizontal(board)!=None:
        return horizontal(board)
    if diag_neg(board)!=None:
        return diag_neg(board)
    if diag_pos(board)!=None:
        return diag_pos(board)
