class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while True:
            sm=numbers[l]+numbers[r]
            if sm>target:
                r-=1
            elif sm<target:
                l+=1
            else:
                return [l+1,r+1]