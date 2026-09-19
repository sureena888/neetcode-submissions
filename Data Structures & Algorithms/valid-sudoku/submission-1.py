class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkDuplicates(singleList: List[str]):
            present = set()
            for i in singleList:
                if i != "." and i in present:
                    return False
                present.add(i)
            return True
            
        for row in board:
            if checkDuplicates(row) == False:
                return False
        
        i = 0
        while i < 9:
            column = []
            for row in board:
                column.append(row[i])
            if checkDuplicates(column) == False:
                return False
            i+=1

        for R in range(0,9,3):
            for C in range(0,9,3):
                square = []
                for r in range(R, R+3):
                    for c in range(C, C+3):
                        square.append(board[r][c])
                if checkDuplicates(square) == False:
                    return False

        return True

        