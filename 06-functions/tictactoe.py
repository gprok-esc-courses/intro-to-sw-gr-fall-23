board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
player = 'X'

def print_board(board, player):
    print(player, "Plays")
    for r in range(3):
        for c in range(3):
            print(board[r][c], end=' ')
        print()

def get_user_input(board):
    row = int(input("Give row (1-3): "))
    col = int(input("Give col (1-3): "))
    if row < 1 or row > 3 or col < 1 or col > 3:
        error = "Invalid row or col"
    elif board[row-1][col-1] != '-':
        error = "Posisition already used"
    else:
        error = None
    return row-1, col-1, error

def update_board(board, player, row, col):
    board[row][col] = player
    return board

def change_player(player):
    player = 'X' if player == 'O' else 'O'
    return player

while True:
    print_board(board, player)
    row, col, error = get_user_input(board)
    if error is None:
        board = update_board(board, player, row, col)
        player = change_player(player)
        # check for winner
        # check for Tie
    else:
        print(error)

        

        