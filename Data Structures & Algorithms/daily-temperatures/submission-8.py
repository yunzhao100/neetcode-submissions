class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # dp(i): in temperatures[i+1:], how many days to see a warmer day than temparatures[i]
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 2, -1, -1):
            curr = temperatures[i]
            k = i + 1
            while k < n:
                if temperatures[k] > curr:
                    res[i] = k - i
                    break
                if res[k] == 0:
                    break
                k = k + res[k]
        return res