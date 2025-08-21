from typing import List

class SudokuSolver:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)

    def solve(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for digit in map(str, range(1, 10)):
                        if self.isValid(board, row, col, digit):
                            board[row][col] = digit
                            if self.solve(board):
                                return True
                            board[row][col] = '.' 
                    return False  
        return True  

    def isValid(self, board: List[List[str]], row: int, col: int, digit: str) -> bool:
      
        for i in range(9):
            if board[row][i] == digit or board[i][col] == digit:
                return False

        
        startRow, startCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == digit:
                    return False

        return True
board =[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]    
solver = SudokuSolver()
solver.solveSudoku(board)

for row in board:
    print(" ".join(row))