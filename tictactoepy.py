#@ Author: Amitrajit Bose
#@ Copyrights Reserved (Just Kidding)
'''Run the script on a GNU-Linux based or Python terminal where the console does not close immediately'''
#Non GUI based Tic Tac Toe Game
board={
'7':' ','8':' ','9':' ',
'4':' ','5':' ','6':' ',
'1':' ','2':' ','3':' ',
}

def printBoard(board):
	print("\t"+board['7']+"|"+board['8']+"|"+board['9'])
	print("\t"+board['4']+"|"+board['5']+"|"+board['6'])
	print("\t"+board['1']+"|"+board['2']+"|"+board['3'])

def verify(ch):
	if((board['1']==board['2'] and board['2']==board['3'] and board['1']==ch) or (board['4']==board['5'] and board['5']==board['6'] and board['4']==ch) or (board['7']==board['8'] and board['8']==board['9'] and board['7']==ch)):		
		print("\nPLAYER "+ch+" WON HORIZONTALLY")
		exit()
	elif((board['1']==board['4'] and board['4']==board['7'] and board['1']==ch) or (board['2']==board['5'] and board['5']==board['8'] and board['2']==ch) or (board['3']==board['6'] and board['6']==board['9'] and board['3']==ch)):		
		print("\nPLAYER "+ch+" WON VERTICALLY")
		exit()
	elif((board['1']==board['5'] and board['5']==board['9'] and board['1']==ch) or (board['3']==board['5'] and board['5']==board['7'] and board['3']==ch)):		
		print("\nPLAYER "+ch+" WON DIAGONALLY")
		exit()

print("\nWELCOME TO CONSOLE TICTACTOE GAME")
print("\nThese are the position names")
print("7|8|9")
print("4|5|6")
print("1|2|3")
print("\nPRESS Q TO QUIT")
print("\nFIRST PLAYER TAKES 'X'\n__________________________")

print("\nEnter Position: ",end="")
p=str(input())
if(p=='Q' or p=='q'):
	print("CLOSING BOARD...CLOSED")
	exit()
board[p]='X'
printBoard(board)

for turn in range(4):
	print("\nEnter Position: ",end="")
	p=str(input())
	if(p=='Q' or p=='q'):
		print("CLOSING BOARD...CLOSED")
		exit()
	board[p]='O'
	printBoard(board)
	verify('O')
	verify('X')
	

	print("\nEnter Position: ",end="")
	p=str(input())
	if(p=='Q' or p=='q'):
		print("CLOSING BOARD...CLOSED")
		exit()
	board[p]='X'
	printBoard(board)
	verify('O')
	verify('X')
	