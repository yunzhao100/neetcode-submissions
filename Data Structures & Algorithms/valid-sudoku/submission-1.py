class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Rdict = defaultdict(set)
        Cdict = defaultdict(set)
        Sdict = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val=='.':
                    continue
                if val in Rdict[r] or val in Cdict[c] or val in Sdict[(r//3,c//3)]:
                    return False
                Rdict[r].add(val)
                Cdict[c].add(val)
                Sdict[(r//3,c//3)].add(val)
        return True