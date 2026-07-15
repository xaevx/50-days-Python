def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(board, player):

    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True

    return False


board = [" " for _ in range(9)]
current_player = "X"

print("=" * 40)
print("        TIC-TAC-TOE")
print("=" * 40)

while True:

    print_board(board)

    try:

        position = int(input(f"Player {current_player}, choose (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Please enter a number between 1 and 9.")
            continue

        if board[position] != " ":
            print("That position is already taken.")
            continue

        board[position] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} Wins!")
            break

        if " " not in board:
            print_board(board)
            print("🤝 It's a Draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    except ValueError:
        print("Please enter a valid number.")