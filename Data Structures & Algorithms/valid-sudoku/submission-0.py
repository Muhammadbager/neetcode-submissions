class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        INPUT:
            board - 2D Array 
                    Each row contains digits 1 - 9 w/o dupes
                    Each col contains digits 1 - 9 w/o dupes
                    Each sub-bozes of the grid must contain the digits 1-9 w/o dupes
        OUTPUT:
              Return True if Board is valid else return False
        Goal: 
            I need to figure out a way to see every sub box is valid and the total board is valid
        Note: 
            Board does not need to be full or solvable to be valid        

        psedocode:

        for every row in range 0 to 9
             have a set
             loop inside the first sub row
                if at the point its a dot
                    continue
                if a number was seen
                    return fals
                add every box in set
        '''
            
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True