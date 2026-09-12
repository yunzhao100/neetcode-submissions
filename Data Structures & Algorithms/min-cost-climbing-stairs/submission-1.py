class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache=[-1]*len(cost)
        def dfs(start):
            if start>=len(cost):
                return 0
            if cache[start]!=-1:
                return cost[start]+cache[start]
            cache[start]=min(dfs(start+1),dfs(start+2))
            return cost[start]+cache[start]
        return min(dfs(0),dfs(1))