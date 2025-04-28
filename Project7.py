



def printBoard(moves):

    print(f"""
      a     b     c    
         |     |     
   1  {moves[0]}  |  {moves[1]}  |  {moves[2]}  
    _____|_____|_____
         |     |     
   2  {moves[3]}  |  {moves[4]}  |  {moves[5]}  
    _____|_____|_____
         |     |     
   3  {moves[6]}  |  {moves[7]}  |  {moves[8]}  
         |     |     
     """)


def initBoard():
    moves = ['-','-','-','-','-','-','-','-','-',]

    printBoard(moves)
    return moves


def getPlayerMove(moves):
    move = input("Enter your move: (eg. a1, b3...) ").lower()
    acceptableMoves = ['a1','b1','c1','a2','b2','c2','a3','b3','c3']

    index = 0
    for x in moves:
        if x != '-':
            acceptableMoves[index] = 'null'
        index += 1

    while move not in acceptableMoves or move == 'null':
        print("Invalid move.")
        move = input("Enter your move: (eg. a1, b3...) ").lower()


    if move == 'a1':
        moves[0] = 'X'
    elif move == 'a2':
        moves[3] = 'X'
    elif move == 'a3':
        moves[6] = 'X'
    elif move == 'b1':
        moves[1] = 'X'
    elif move == 'b2':
        moves[4] = 'X'
    elif move == 'b3':
        moves[7] = 'X'
    elif move == 'c1':
        moves[2] = 'X'
    elif move == 'c2':
        moves[5] = 'X'
    elif move == 'c3':
        moves[8] = 'X'

    return moves



def getComputerMove(moves):
    from random import randint
    move = randint(0,8)

    while moves[move] != '-':
        move = randint(0,8)

    moves[move] = '0'

    return moves

def checkWin(moves):
    if moves[0] == moves[1] and moves[0] == moves[2]:
        if moves[0] == 'X':
            return "player"
        elif moves[0] == '0':
            return "computer"
    elif moves[3] == moves[4] and moves[3] == moves[5]:
        if moves[3] == 'X':
            return "player"
        elif moves[3] == '0':
            return "computer"
    elif moves[6] == moves[7] and moves[6] == moves[8]:
        if moves[6] == 'X':
            return "player"
        elif moves[6] == '0':
            return "computer"
    elif moves[0] == moves[3] and moves[0] == moves[6]:
        if moves[0] == 'X':
            return "player"
        elif moves[0] == '0':
            return "computer"
    elif moves[1] == moves[4] and moves[1] == moves[7]:
        if moves[1] == 'X':
            return "player"
        elif moves[1] == '0':
            return "computer"
    elif moves[2] == moves[5] and moves[2] == moves[8]:
        if moves[2] == 'X':
            return "player"
        elif moves[2] == '0':
            return "computer"
    elif moves[0] == moves[4] and moves[0] == moves[8]:
        if moves[0] == 'X':
            return "player"
        elif moves[0] == '0':
            return "computer"
    elif moves[2] == moves[4] and moves[2] == moves[6]:
        if moves[2] == 'X':
            return "player"
        elif moves[2] == '0':
            return "computer"

    if '-' in moves:
        return "continue"
    else:
        return "draw"


def playRound(moves, turn):
    if turn == 'player':
        moves = getPlayerMove(moves)
    else:
        moves = getComputerMove(moves)

    printBoard(moves)

    return moves

def playGame():
    moves = initBoard()
    turn = 'player'
    state = checkWin(moves)

    while state == 'continue':
        playRound(moves, turn)
        if turn == 'player':
            turn = 'computer'
        else:
            turn = 'player'
        state = checkWin(moves)

    if state == 'player':
        print("Congratulations! You won!")
    elif state == 'computer':
        print("You lost. Better luck next time.")
    elif state == 'draw':
        print("The game ends in a draw.")


playGame()








