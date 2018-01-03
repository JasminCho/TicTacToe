

def getMoves(currentPlayer, move, p1, p2):
	symbol = ''
	if currentPlayer == 0:
		symbol = p1
		# print("Player 1's symbol is " + p1)
		# print("The current player's symbol is " + symbol)
	elif currentPlayer == 1:
		symbol = p2
	
	boardState[move - 1] = symbol

	printBoard()
	checkState(boardState, symbol, currentPlayer)

def printBoard():
	pos1 = boardState[0]
	pos2 = boardState[1]
	pos3 = boardState[2]
	pos4 = boardState[3]
	pos5 = boardState[4]
	pos6 = boardState[5]
	pos7 = boardState[6]
	pos8 = boardState[7]
	pos9 = boardState[8]

	board = """
	  %s | %s | %s
	-------------
	  %s | %s | %s
	-------------
	  %s | %s | %s
	"""
	print(board %(pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9))

def checkState(boardState, symbol, currentPlayer):
	if (boardState[0] == boardState[1] == boardState[2] == symbol) or (boardState[3] == boardState[4] == boardState[5] == symbol) or (boardState[6] == boardState[7] == boardState[8] == symbol) or (boardState[0] == boardState[3] == boardState[6] == symbol) or (boardState[1] == boardState[4] == boardState[7] == symbol) or (boardState[2] == boardState[5] == boardState[8] == symbol) or (boardState[0] == boardState[4] == boardState[8] == symbol) or (boardState[2] == boardState[4] == boardState[6] == symbol):
		if currentPlayer == 0:
			print(player1 + " wins!")
			quit()
		elif currentPlayer == 1:
			print(player2 + " wins!")
			quit()

# Intro
print("\tWelcome to Tic Tac Toe!")
player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")
print("Welcome " + player1 + " and " + player2 + "!")

# 0 is player 1, 1 is player 2
currentPlayer = 0
boardState = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
p1Symbol = ' '
p2Symbol = ' '


if currentPlayer == 0:
	print("It's " + player1 + "'s turn!")
	p1Symbol = input(player1 + " please choose X or O: ").upper()
	if p1Symbol == 'X':
		p2Symbol = 'O'
	elif p1Symbol == 'O':
		p2Symbol = 'X'
	else:
		print("Error: Incorrect Input, has to be X or O")
	print(player1 + " is " + p1Symbol + " and " + player2 + " is " + p2Symbol)
elif currentPlayer == 1:
	print("It's " + player2 + "'s turn!")
	p2Symbol = input(player1 + " please choose X or O: ").upper()
	if p2Symbol == 'X':
		p1Symbol = 'O'
	elif p2Symbol == 'O':
		p1Symbol = 'X'
	else:
		print("Error: Incorrect Input, has to be X or O")
	print(player1 + " is " + p1Symbol + " and " + player2 + " is " + p2Symbol)
else:
	print("There's something wrong... Can't determine turn")

while ' ' in boardState:
	if currentPlayer == 0:
		move = input(player1 + ", pick a position 1 - 9: ")
		if boardState[int(move)-1] != ' ':
			print("Pick another spot, there's already a mark there!")
			continue
		getMoves(currentPlayer, int(move), p1Symbol, p2Symbol)
		currentPlayer = 1
	elif currentPlayer == 1:
		move = input(player2 + ", pick a position 1 - 9: ")
		if boardState[int(move)-1] != ' ':
			print("Pick another spot, there's already a mark there!")
			continue
		getMoves(currentPlayer, int(move), p1Symbol, p2Symbol)
		currentPlayer = 0
else:
	print("It's a tie!")