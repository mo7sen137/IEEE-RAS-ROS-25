
def main():
    m =input (f"Helo there ! This is X,O game (press c to continue): ")
    m= m.lower ()
    while m != "c":
            print ("Enter c ylaaaa !!")
            m =input (f"Helo there ! This is X,O game (press c to continue): ")
            m= m.lower ()
    if m == "c":
            player_one =str(input (f"Enter 1st player name: "))
            player_two =str(input (f"Enter 2nd player name: "))
            print (f"Hi {player_one} and {player_two}")

            Hi=input (f"(press s to start the game): ")
            while Hi != "s":
                print ("press s yaaam !!")
                Hi=input (f"(press s to start the game): ")
                Hi=Hi.lower()

            if Hi == "s":
                print ("Wellcome to theTic-Tac-Toe game !!")


    player_one_symbol=input (f"Plz {player_one} Choose Your Symbol (X or O): ")
    player_one_symbol=player_one_symbol.upper()

    while True:
        if player_one_symbol == "X":
                print("Done !!")
                break
        elif player_one_symbol == "O":
                print ("Done !!")
                break
        else :
                continue

    if player_one_symbol == "X":
            player_two_symbol="O"
    else:
            player_two_symbol = "X"
            player_one_symbol = "O"

    print (f"{player_one}, your symbol is '{player_one_symbol}' and {player_two},  your symbol is '{player_two_symbol}'")


    

    global current_player
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    current_player = player_one
    players = {player_one:player_one_symbol, player_two:player_two_symbol}

    def print_board():
        print("Current Board:")
        for i, row in enumerate(board):
            print(" | ".join(row))
            if i < 2:
                print("---------")

    D=input (f"Enter (D) to Continue: ")
    D=D.upper()
    while True:
        if D != "D":    
            print ("Enter 'D' ylaaaa !!")
            D=input (f"Enter (D) to Continue: ")
            D=D.upper()
            continue
        elif D == "D":
            print ("DONE !!")
            break

    def check_winner():
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2]:
                return row[0]
        
        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col]:
                return board[0][col]
        
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
        
        return None


    def is_board_full():
        for row in board:
            for cell in row:
                if cell in "123456789":
                    return False
        return True


    def make_move():
        global current_player
        while True:
            try:
                position = int(input(f"{current_player}, choose a position (1-9): "))
                if 1 <= position <= 9:
                    row = (position - 1) // 3  # Convert to row index (0-2)
                    col = (position - 1) % 3   # Convert to column index (0-2)
                    
                    
                    if board[row][col] in "123456789":
                        board[row][col] = players [current_player]
                        current_player = player_two if current_player == player_one else player_one  # Switch player
                        break
                    else:
                        print("Position already taken! Try again.")
                else:
                    print("Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input! Enter a number (1-9).")

    game_over = False
    while not game_over:
        print_board()
        make_move()
        check_winner()

        winner_symbol = check_winner()
        if winner_symbol == player_one_symbol:
            print (f"{player_one} wins! Congratulations!")
            break
        elif winner_symbol == player_two_symbol:
            print (f"{player_two} wins! Congratulations!")
            break
        elif is_board_full():
            print_board()
            print("\n😐 It's a draw! No more moves left.")
            break

if __name__ == "__main__":
    main()