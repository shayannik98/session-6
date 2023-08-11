print("welcome to x/o game: ")
#create by shayan nikpour

from pyfiglet import Figlet


def game():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()


def check1():
    # amudi1
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("bazikon shomare 1 winner  X ")
        return True
    # amudi 2
    elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print("bazikon shomare 1 winner  X")
        return True
    # amudi 3
    elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print("bazikon shomare 1 winner  X")
        return True
    # ofoghi 1
    elif game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print("bazikon shomare 1 winner  X")
        return True
    # ofoghi 2
    elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("bazikon shomare 1 winner  X")
        return True
    # ofoghi 3
    elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("bazikon shomare 1 winner  X")
        return True
    # movarab 1
    elif game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("bazikon shomare 1 winner  X")
        return True
    # movarab 2
    elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
        print("bazikon shomare 1 winner  X")
        return True
    return False


def check2():
    # AMUDI 1
    if game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print("player 2 is winner O ")
        return True
    # amudi 2
    elif game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        print("player 2 is winner O ")
        return True
    # amudi3
    elif game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
        print("player 2 is winner O ")
        return True
    # ofoghi 1
    elif game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print("player 2 is winner O ")
        return True
    # ofoghi 2
    elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print("player 2 is winner O ")
        return True
    # ofoghi 3
    elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("player 2 is winner O ")
        return True
    # movarab 1
    elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("player 2 is winner O ")
        return True
    # movarab 2
    elif game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
        print("player 2 is winner O ")
        return True
    return False


f = Figlet(font='slant')
print(f.renderText('Tic-Tac-Toe'))

game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]
game()

turns = 0

while True:
    # Player1
    print("Player 1: ")
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    if 0 <= row <= 2 and 0 <= col <= 2:
        if game_board[row][col] == "-":
            game_board[row][col] = "X"
            game()
            if check1():
                break
            turns += 1
        else:
            print("tekrari! mojadad entekhab konid.")
    else:
        print("beyne baze 0,2 entekhab konid.")

    # Check for tie
    if turns == 9:
        print("no winner! draw")
        break

    # Player2
    print("Player 2: ")
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    if 0 <= row <= 2 and 0 <= col <= 2:
        if game_board[row][col] == "-":
            game_board[row][col] = "O"
            game()
            if check2():
                break
            turns += 1
        else:
            print("tekrari! mojadad entekhab konid..")
    else:
        print("beyne baze 0,2 entekhab konid.")

    # Check for tie
    if turns == 9:
        print("NO WINNER, draw!")
        break