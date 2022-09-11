def printBoard(board):
    '''Prints out the entire board.'''

    print(board[1] + '|' + board[2] + '|' + board[3])
    print("-+-+-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-+-+-")
    print(board[7] + '|' + board[8] + '|' + board[9])


def spaceIsFree(position):
    '''Checks if a position on the board is free.'''

    return True if board[position] == ' ' else False


def checkDraw(board):
    '''Checks if board is in a position of draw.'''
    for value in board.values():
        if value == ' ':
            return False
    return True


def checkWin(board):
    '''Used to check if the board is in a condition where any of the player has won.'''
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True
    else:
        return False


def checkAIWin(mark):
    '''Used to check if the board is in a condition where any of the AIs has won in the minimax function'''
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == mark:
        return True
    else:
        return False


def insertLetter(letter, position):
    '''This method is used for adding the player's or bot's move to the board.'''
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)

        if checkDraw(board):
            print("The game is a draw.")
            exit()

        if checkWin(board):
            if letter == "X":
                print("Bot wins!")
                exit()
            else:
                print("You win!")
                exit()

        return

    else:
        print("Please select another position.")
        position1 = int(input("Enter the position: "))
        insertLetter(letter, position1)
        return


def minimax(board, depth, isMaximizing):
    if checkAIWin(bot):
        return 1

    elif checkAIWin(player):
        return -1

    elif checkDraw(board):
        return 0

    if isMaximizing:
        # if computer is playing
        bestScore = -800

        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score

        return bestScore

    else:
        bestScore = 800

        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, 0, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score

        return bestScore


def playerMove():
    '''Takes a value from player to make a move on the board.'''
    number = False
    while not number:
        position = input("Enter a position for O from 0 to 9: ")
        if position.isnumeric():
            number = True
    insertLetter(player, int(position))
    return


def botMove():
    '''Takes no input. This is the AI playing.'''
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        # Calculating score for each position in order to get best position
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


if __name__ == "__main__":
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    player = 'O'
    bot = 'X'
    printBoard(board)
    while not checkWin(board):
        playerMove()
        botMove()
