class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        dic={}
        def dp(i):
            if i>=n-1: return 0
            if i in dic: return dic[i]
            j=i+1
            while j<n and temperatures[j]<=temperatures[i]:
                wait_j=dp(j)
                if wait_j==0:
                    dic[i]=0
                    return dic[i]
                j+=wait_j
            if j>=n:
                dic[i]=0
                return dic[i]
            else:
                dic[i]=j-i
                return dic[i]
        return [dp(i) for i in range(n)]