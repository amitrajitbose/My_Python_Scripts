#Non GUI based Tic Tac Toe Game
board={
'top-L':' ','top-M':' ','top-R':' ',
'mid-L':' ','mid-M':' ','mid-R':' ',
'low-L':' ','low-M':' ','low-R':' ',}

def printBoard(board):
	print(board['top-L']+"|"+board['top-M']+"|"+board['top-R'])
	print("-------")
	print(board['mid-L']+"|"+board['mid-M']+"|"+board['mid-R'])
	print("-------")
	print(board['low-L']+"|"+board['low-M']+"|"+board['low-R'])

print("\n\nWELCOME TO CONSOLE TICTACTOE GAME")
print("\nThese are the positions")
print("top-L ,top-M ,top-R")
print("mid-L ,mid-M ,mid-R")
print("mid-L ,mid-M ,mid-R")
print("\nPRESS Q TO QUIT")
print("\nFIRST PLAYER TAKES 'X'\n__________________________")

print("\nEnter position: ",end="")
p=str(input())
if(p=='Q' or p=='q'):
	print("CLOSING BOARD...CLOSED")
	exit()
board[p]='X'
printBoard(board)

for turn in range(4):
	print("\nEnter position: ",end="")
	p=str(input())
	if(p=='Q' or p=='q'):
		print("CLOSING BOARD...CLOSED")
		exit()
	board[p]='O'
	printBoard(board)

	print("Enter position: ",end="")
	p=str(input())
	if(p=='Q' or p=='q'):
		print("CLOSING BOARD...CLOSED")
		exit()
	board[p]='X'
	printBoard(board)