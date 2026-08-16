class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Checking rows
        for i in range(9):
            d1 = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in d1:
                    return False
                else:
                    d1[board[i][j]] = 1

        # Checking columns
        for i in range(9):
            d1 = {}
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in d1:
                    return False
                else:
                    d1[board[j][i]] = 1

        # Checking 3X3
        d={}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                box_id = (i//3,j//3)
                if box_id not in d:
                    d[box_id] = {}
                if val in d[box_id]:
                    return False
                else:
                    d[box_id][val] = 1
        return True













