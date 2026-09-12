class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Rdic=defaultdict(set)
        Cdic=defaultdict(set)
        Sdic=defaultdict(set)
        for r in range(9):
            for c in range(9):
                n=board[r][c]
                if n=='.':
                    continue
                if n in Rdic[r] or n in Cdic[c] or n in Sdic[tuple([r//3,c//3])]:
                    return False
                Rdic[r].add(n)
                Cdic[c].add(n)
                Sdic[tuple([r//3,c//3])].add(n)
        return True