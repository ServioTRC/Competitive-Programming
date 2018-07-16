board = [['0' for _ in range(8)] for _ in range(8)]

def print_board():
    for ele in board:
        print(ele)

def clean_board():
    global board
    board = [['0' for _ in range(8)] for _ in range(8)]

def creating_board(fen):
    rows = fen.split("/")
    for i in range(8):
        board_pos = 0
        for ele in rows[i]:
            if ele.isdigit():
                board_pos += int(ele)
            else:
                board[i][board_pos] = ele
                board_pos += 1

def counting_spaces():
    count = 0
    for ele in board:
        for ele2 in ele:
            if ele2 == '0':
                count += 1
    print(count)

def mark_knights(i, j):
    #Up
    if i-2 >= 0 and j-1 >= 0:
        if board[i-2][j-1] == '0':
            board[i-2][j-1] = 'X'
    if i-2 >= 0 and j+1 < 8:
        if board[i-2][j+1] == '0':
            board[i-2][j+1] = 'X'
    #Down
    if i+2 < 8 and j-1 >= 0:
        if board[i+2][j-1] == '0':
            board[i+2][j-1] = 'X'
    if i+2 < 8 and j+1 < 8:
        if board[i+2][j+1] == '0':
            board[i+2][j+1] = 'X'
    #Left
    if j+2 < 8 and i-1 >= 0:
        if board[i-1][j+2] == '0':
            board[i-1][j+2] = 'X'
    if j+2 < 8 and i+1 < 8:
        if board[i+1][j+2] == '0':
            board[i+1][j+2] = 'X'
    #Right
    if j-2 >= 0 and i-1 >= 0:
        if board[i-1][j-2] == '0':
            board[i-1][j-2] = 'X'
    if j-2 >= 0 and i+1 < 8:
        if board[i+1][j-2] == '0':
            board[i+1][j-2] = 'X'

def mark_bishop(i, j):
    #Left-Up
    pos_i = i - 1
    pos_j = j - 1
    while (pos_i >= 0 and pos_j >= 0):
        if board[pos_i][pos_j] == "0":
            board[pos_i][pos_j] = "X"
        elif board[pos_i][pos_j] == "X":
            pass
        else:
            break
        pos_i -= 1
        pos_j -= 1
    #Left-Down
    pos_i = i + 1
    pos_j = j - 1
    while (pos_i < 8 and pos_j >= 0):
        if board[pos_i][pos_j] == '0':
            board[pos_i][pos_j] = 'X'
        elif board[pos_i][pos_j] == 'X':
            pass
        else:
            break
        pos_i += 1
        pos_j -= 1
    #Right-Up
    pos_i = i - 1
    pos_j = j + 1
    while (pos_i >= 0 and pos_j < 8):
        if board[pos_i][pos_j] == '0':
            board[pos_i][pos_j] = 'X'
        elif board[pos_i][pos_j] == 'X':
            pass
        else:
            break
        pos_i -= 1
        pos_j += 1
    #Right-Down
    pos_i = i + 1
    pos_j = j + 1
    while (pos_i < 8 and pos_j < 8):
        if board[pos_i][pos_j] == '0':
            board[pos_i][pos_j] = 'X'
        elif board[pos_i][pos_j] == 'X':
            pass
        else:
            break
        pos_i += 1
        pos_j += 1

def mark_rook(i, j):
    #UP
    pos_i = i - 1
    while(pos_i >= 0):
        if board[pos_i][j] == '0':
            board[pos_i][j] = 'X'
        elif board[pos_i][j] == 'X':
            pass
        else:
            break
        pos_i -= 1
    #Down
    pos_i = i + 1
    while(pos_i < 8):
        if board[pos_i][j] == '0':
            board[pos_i][j] = 'X'
        elif board[pos_i][j] == 'X':
            pass
        else:
            break
        pos_i += 1
    #Right
    pos_j = j + 1
    while(pos_j < 8):
        if board[i][pos_j] == '0':
            board[i][pos_j] = 'X'
        elif board[i][pos_j] == 'X':
            pass
        else:
            break
        pos_j += 1
    #Left
    pos_j = j - 1
    while(pos_j >= 0):
        if board[i][pos_j] == '0':
            board[i][pos_j] = 'X'
        elif board[i][pos_j] == 'X':
            pass
        else:
            break
        pos_j -= 1

def mark_king(i, j):
    #Up-Left
    if i-1 >= 0 and j-1 >= 0:
        if board[i-1][j-1] == '0':
            board[i-1][j-1] = 'X'
    #Up
    if i-1 >= 0:
        if board[i-1][j] == '0':
            board[i-1][j] = 'X'
    #Up-Right
    if i-1 >= 0 and j+1 < 8:
        if board[i-1][j+1] == '0':
            board[i-1][j+1] = 'X'
    #Right
    if j+1 < 8:
        if board[i][j+1] == '0':
            board[i][j+1] = 'X'
    #Down-Right
    if i+1 < 8 and j+1 < 8:
        if board[i+1][j+1] == '0':
            board[i+1][j+1] = 'X'
    #Down
    if i+1 < 8:
        if board[i+1][j] == '0':
            board[i+1][j] = 'X'
    #Down-Left
    if i+1 < 8 and j-1 >= 0:
        if board[i+1][j-1] == '0':
            board[i+1][j-1] = 'X'
    #Left
    if j-1 >= 0:
        if board[i][j-1] == '0':
            board[i][j-1] = 'X'

def marking_movements():
    for i in range(8):
        for j in range(8):
            #Black pawn
            if board[i][j] == 'p':
                if j+1 < 8 and i+1 < 8:
                    if board[i+1][j+1] == '0':
                        board[i+1][j+1] = 'X'
                if j-1 >= 0 and i+1 < 8:
                    if board[i+1][j-1] == '0':
                        board[i+1][j-1] = 'X'
            #White pawn
            elif board[i][j] == 'P':
                if j-1 >= 0 and i-1 >= 0:
                    if board[i-1][j-1] == '0':
                        board[i-1][j-1] = 'X'
                if j+1 < 8 and i-1 >= 0:
                    if board[i-1][j+1] == '0':
                        board[i-1][j+1] = 'X'
            #Knights
            elif board[i][j] == 'N' or board[i][j] == 'n':
                mark_knights(i, j)
            #Bishop
            elif board[i][j] == 'B' or board[i][j] == 'b':
                mark_bishop(i, j)
            #Rook
            elif board[i][j] == 'R' or board[i][j] == 'r':
                mark_rook(i, j)
            #Queen
            elif board[i][j] == 'Q' or board[i][j] == 'q':
                mark_bishop(i, j)
                mark_rook(i, j)
            #King
            elif board[i][j] == 'K' or board[i][j] == 'k':
                mark_king(i, j)


def main():
    try:
        while True:
            fen = input()
            creating_board(fen)
            marking_movements()
            #print_board()
            counting_spaces()
            clean_board()
    except EOFError as e:
        pass

if __name__ == "__main__":
    main()