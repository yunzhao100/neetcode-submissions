class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        if len(A)>len(B):
            A,B=B,A
        lenA=len(A)
        lenB=len(B)
        total=lenA+lenB
        half=total//2
        l,r=0,lenA-1
        while True:
            m=(l+r)//2
            pointerB=half-m-2
            Aleft=A[m] if m>=0 else float('-infinity')
            Aright=A[m+1] if m+1<lenA else float('infinity')
            Bleft=B[pointerB] if pointerB>=0 else float('-infinity')
            Bright=B[pointerB+1] if pointerB+1<lenB else float('infinity')
            if Aleft<=Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=m-1
            else:
                l=m+1