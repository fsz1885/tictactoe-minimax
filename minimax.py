def grid(char):
    if char == 'q':
        return 0
    elif char == 'w':
        return 1
    elif char == 'e':
        return 2
    elif char == 'a':
        return 3
    elif char == 's':
        return 4
    elif char == 'd':
        return 5
    elif char == 'z':
        return 6
    elif char == 'x':
        return 7
    elif char == 'c':
        return 8
    else:
        return None


def iswin(board):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for combination in winning_combinations:
        i, j, k = combination[0], combination[1], combination[2]
        if board[i] == board[j] and board[i] == board[k]:
            if board[i] != " ":
                return board[i]


def draw(board):
    return not " " in board


def utility(player, board):
    win = iswin(board)
    if win:
        if win == player:
            return 1
        else:
            return -1
    return 0


def opponent(player):
    if player == "X":
        return "O"
    return "X"


def available_move(board):
    lst = []
    for i in range(len(board)):
        if board[i] == " ":
            lst.append(i)
    return lst


def minimax(board, current_player, max_player="O"):
    if iswin(board):
        if iswin(board) == max_player:
            return 1, None
        else:
            return -1, None

    if draw(board):
        return 0, None

    moves = available_move(board)

    if current_player == max_player:
        best_move = None
        best_utility = float("-inf")
        for move in moves:
            new_board = board.copy()
            new_board[move] = current_player
            new_utility, _ = minimax(new_board, opponent(current_player),
                                     max_player)

            if new_utility > best_utility:
                best_utility = new_utility
                best_move = move
        return best_utility, best_move

    else:
        best_move = None
        best_utility = float("inf")
        for move in moves:
            new_board = board.copy()
            new_board[move] = current_player
            new_utility, _ = minimax(new_board, opponent(current_player),
                                     max_player)

            if new_utility < best_utility:
                best_utility = new_utility
                best_move = move
        return best_utility, best_move


def render(lst):
    print("_________")
    for i in range(0, 9, 3):
        print("|", lst[i], lst[i + 1], lst[i + 2], "|")
    print("---------")


def player_move(lst, player):
    i = 1
    while i:
        print("move: ")
        char = input()
        move = grid(char)
        if move is not None and lst[move] == " ":
            lst[move] = player
            render(lst)
            i = 0
        else:
            print("invalid move!")


def ai_move(lst, player):
    if player == "X":
        move = minimax(lst, player, max_player="X")[1]
    else:
        move = minimax(lst, player, max_player="O")[1]
    lst[move] = player
    render(lst)


def get_mode():
    while True:
        print("Choose Mode:")
        print("1. Player vs Player")
        print("2. Player vs AI")
        print("3. AI vs Player")
        print("4. AI vs AI")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            return "H", "H"
        elif choice == "2":
            return "H", "A"
        elif choice == "3":
            return "A", "H"
        elif choice == "4":
            return "A", "A"
        else:
            print("Invalid choice. Try again.")


def make_move(board, player, player_type):
    if player_type == "H":
        player_move(board, player)
    else:
        ai_move(board, player)


def launch():
    p1, p2 = get_mode()

    board = [" " for _ in range(9)]
    render(board)

    player = "X"

    while True:
        if iswin(board):
            print(iswin(board), "Wins!")
            break
        if draw(board):
            print("Draw!")
            break

        if player == "X":
            make_move(board, player, p1)
        else:
            make_move(board, player, p2)

        player = opponent(player)


if __name__ == "__main__":
    launch()
