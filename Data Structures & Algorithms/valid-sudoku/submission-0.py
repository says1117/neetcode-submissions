class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #cols
        for r in range(9):
            inset = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] not in inset:
                    inset.add(board[r][c])
                else:
                    return False

        for c in range(9):
            inset = set()
            for r in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] not in inset:
                    inset.add(board[r][c])
                else:
                    return False

        for i in range(9):
            row = (i // 3) * 3
            col = (i % 3) * 3
            inset = set()
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if board[r][c] == '.':
                        continue
                    if (board[r][c] not in inset):
                        inset.add(board[r][c])
                    else:
                        return False

        return True





