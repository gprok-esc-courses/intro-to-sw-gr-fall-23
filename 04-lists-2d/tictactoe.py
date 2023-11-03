board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
player = 'X'

while True:
    # Who plays
    print(player, "Plays")

    # Display board
    for r in range(3):
        for c in range(3):
            print(board[r][c], end=' ')
        print()

    # Get row, col from user
    row = int(input("Give row (1-3): "))
    col = int(input("Give col (1-3): "))

    # Check row, col if ok update board and change user
    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid row or col")
    elif board[row-1][col-1] != '-':
        print("Posisition already used")
    else:
        board[row-1][col-1] = player
        player = 'X' if player == 'O' else 'O'
        
        # check for winner

        # check for Tie