class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows,Cols=len(matrix),len(matrix[0])
        l,r=0,Rows*Cols-1
        while l<=r:
            m=(l+r)//2
            row,col=m//Cols,m%Cols
            val=matrix[row][col]
            if val==target:
                return True
            elif val>target:
                r=m-1
            else:
                l=m+1
        return False