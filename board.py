def play(board,col,player):
    if col<1 and col>7:
        return None
    else:
        for row in range(5,-1,-1):
            if board[row][col-1]==0:
                board[row][col-1] = player
                return board
    return None
