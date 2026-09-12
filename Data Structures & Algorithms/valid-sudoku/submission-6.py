class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dic,col_dic,squ_dic=defaultdict(set),defaultdict(set),defaultdict(set)
        for row in range(9):
            for col in range(9):
                val=board[row][col]
                if val=='.':
                    continue
                if val in row_dic[row] or val in col_dic[col] or val in squ_dic[(row//3,col//3)]:
                    return False
                row_dic[row].add(val)
                col_dic[col].add(val)
                squ_dic[(row//3,col//3)].add(val)
        return True