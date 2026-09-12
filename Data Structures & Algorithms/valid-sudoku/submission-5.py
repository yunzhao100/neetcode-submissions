class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Rdic=defaultdict(set)
        Cdic=defaultdict(set)
        Sdic=defaultdict(set)
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val==".":
                    continue
                if val in Rdic[r] or val in Cdic[c] or val in Sdic[(r//3,c//3)]:
                    return False
                Rdic[r].add(val)
                Cdic[c].add(val)
                Sdic[(r//3,c//3)].add(val)
        return True