class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])
        l,r=0,Rows*Cols-1
        while l<=r:
            m=l+(r-l)//2
            midRow, midCol=m//Cols, m%Cols
            if matrix[midRow][midCol]>target:
                r=m-1
            elif matrix[midRow][midCol]<target:
                l=m+1
            else:
                return True
        return False