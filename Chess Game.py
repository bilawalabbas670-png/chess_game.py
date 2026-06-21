board = [
    ["r","n","b","q","k","b","n","r"],
    ["p","p","p","p","p","p","p","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    ["P","P","P","P","P","P","P","P"],
    ["R","N","B","Q","K","B","N","R"]
]

turn = "white"

def print_board():
    print("\n  a b c d e f g h")
    for i in range(8):
        print(8-i, end=" ")
        for j in range(8):
            print(board[i][j], end=" ")
        print()
    print()

def valid_turn(piece):
    if turn == "white" and piece.isupper():
        return True
    if turn == "black" and piece.islower():
        return True
    return False

def move_piece():
    global turn

    move = input(f"{turn} move (e2 e4): ").split()

    if len(move) != 2:
        print("Invalid input")
        return

    cols = "abcdefgh"

    sx = 8 - int(move[0][1])
    sy = cols.index(move[0][0])

    ex = 8 - int(move[1][1])
    ey = cols.index(move[1][0])

    piece = board[sx][sy]

    if piece == ".":
        print("No piece selected")
        return

    if not valid_turn(piece):
        print("Wrong turn!")
        return

    # Basic pawn rule (simple)
    if piece.lower() == "p":
        if sy == ey and board[ex][ey] == ".":
            if (piece == "P" and ex == sx-1) or (piece == "p" and ex == sx+1):
                pass
            else:
                print("Invalid pawn move")
                return

    board[sx][sy] = "."
    board[ex][ey] = piece

    turn = "black" if turn == "white" else "white"


while True:
    print_board()
    move_piece()