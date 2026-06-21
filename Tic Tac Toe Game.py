board = [" " for _ in range(9)]
current_player = "X"

def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# RULE 1: valid move check
def valid_move(pos):
    if pos < 0 or pos > 8:
        return False
    if board[pos] != " ":
        return False
    return True

# RULE 2: win conditions
def check_winner():
    win_rules = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in win_rules:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

# RULE 3: draw condition
def check_draw():
    return " " not in board

def play_turn():
    global current_player

    try:
        pos = int(input(f"Player {current_player} enter position (1-9): ")) - 1
    except:
        print("Invalid input! Number enter karo.")
        return

    # RULE apply
    if not valid_move(pos):
        print("Invalid move! Try again.")
        return

    board[pos] = current_player

    # check win
    winner = check_winner()
    if winner:
        print_board()
        print(f"🎉 Player {winner} wins!")
        exit()

    # check draw
    if check_draw():
        print_board()
        print("Match Draw!")
        exit()

    # RULE: turn change
    current_player = "O" if current_player == "X" else "X"


# GAME LOOP
while True:
    print_board()
    play_turn()