class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set) # key will be a pair/tuple (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                # check in row, this num appeared before?
                if board[r][c] in rows[r]:
                    return False
                
                # check in col, this num appeared before?
                if board[r][c] in cols[c]:
                    return False
                
                # check in that square, if this number appeared before?
                if board[r][c] in sqrs[(r // 3, c // 3)]:
                    return False
                
                # update the sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqrs[(r // 3, c // 3)].add(board[r][c])
            
        return True