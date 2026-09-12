class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        if len(A)>len(B): A,B=B,A
        len_A,len_B=len(A),len(B)
        total=len_A+len_B
        half=total//2
        l,r=0,len_A-1
        while True:
            pointer_A=(l+r)//2
            pointer_B=half-(pointer_A+1)-1
            A_left=A[pointer_A] if pointer_A>=0 else float('-inf')
            A_right=A[pointer_A+1] if pointer_A+1<len_A else float('inf')
            B_left=B[pointer_B] if pointer_B>=0 else float('-inf')
            B_right=B[pointer_B+1] if pointer_B+1<len_B else float('inf')
            if A_left<=B_right and B_left<=A_right:
                if total%2:
                    return min(A_right,B_right)
                else:
                    return (max(A_left,B_left)+min(A_right,B_right))/2
            elif A_left>B_right:
                r=pointer_A-1
            elif B_left>A_right:
                l=pointer_A+1