class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        if amount in coins: return 1
        dic={0: 0}
        def dp(i):
            if i < 0: return -1
            if i in dic: return dic[i]
            temp = amount + 1
            for c in coins:
                res = dp(i - c)
                if res >= 0:
                    temp = min(temp, 1 + res)
            dic[i] = temp if temp <= amount else -1
            return dic[i]
        return dp(amount)