def initialize_board(board,n):
	for key in ['queen', 'row', 'col', 'nwtose', 'swtone']:
		board[key] = {}
			
	for i in range(n):
		board['queen'][i] = -1
		board['row'][i] = 0
		board['col'][i] = 0
		
	for j in range(-(n-1),(n-1)):
		board['nwtose'][j] = 0
	
	for k in range(0,2*(n-1)):
		board['swtone'][k] = 0

def check_free(board, c, i):
	if board['row'][i] == 0 and board['col'][c] == 0 and board['nwtose'][c - i] == 0 and board['swtone'][c + i] == 0:
		return True  
	else:
		return False

def addqueen(board, j, r):
	board['queen'][r] = j
	board['row'][r] = 1
	board['col'][j] = 1
	board['nwtose'][j-r] = 1
	board['swtone'][j+r] = 1
	
def undoqueen(board, c, r):
	board['queen'][r] = -1
	board['row'][r] = 0
	board['col'][c] = 0
	board['nwtose'][c - r] = 0
	board['swtone'][c + r] = 0
	

def placequeen(board,i):
	n = len(board['queen'].keys())
	for c in range(n):
		if check_free(board,c,i):
			addqueen(board, c, i)
			if i == n - 1:
				return True
			else:
				extendsolution = placequeen(board,i+1)
			if extendsolution:
				return True
			else:
				undoqueen(board, c, i)
	else:
		return False

def printboard(board,n):
	for row in sorted(board['queen'].keys()):
		print((row,board['queen'][row]))
			
def printboardpretty(board, n):
	for row in range(n):
		print("")
		print("|", end="")
		for column in range(n):
			if board['queen'][row] == column:
				print("Q|", end="")
			else:
				print("_|", end="")



board = {}
n = int(input("Enter the size of the chess board: "))
initialize_board(board,n)
try:
	if placequeen(board,0):
		#print(board)
		#printboard(board, n)  prints the location of the queens on the chess board
		printboardpretty(board, n)	# Prints the Queens on the board
except:
	print("not possible!!")
	
	

