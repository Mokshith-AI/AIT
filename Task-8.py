# Python3 program to solve N Queen Problem using backtracking
global N
N = 5   # <--- Change this value to any board size you want

def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end=" ")
		print()

def isSafe(board, row, col):
	# Check this row on left side
	for i in range(col):
		if board[row][i] == 1:
			return False

	# Check upper diagonal on left side
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	# Check lower diagonal on left side
	for i, j in zip(range(row, N, 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False
	return True

def solveNQUtil(board, col):
	# Base case: If all queens are placed then return true
	if col >= N:
		return True

	# Try placing queen in all rows one by one
	for i in range(N):
		if isSafe(board, i, col):
			board[i][col] = 1
			if solveNQUtil(board, col + 1) == True:
				return True
			board[i][col] = 0
	return False

def solveNQ():
	board = [[0 for _ in range(N)] for _ in range(N)]
	if solveNQUtil(board, 0) == False:
		print("Solution does not exist")
		return False
	printSolution(board)
	return True

# Driver Code
if __name__ == '__main__':
	solveNQ()
