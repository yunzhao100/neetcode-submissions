class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        
        def dp(i):
            if i >= n:
                return
            # 确保右侧元素先被处理
            if i < n - 1:
                dp(i + 1)
            # 处理当前元素i
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
                else:
                    if res[j] == 0:  # j之后没有更高温度
                        res[i] = 0
                        break
                    j += res[j]      # 跳到j之后的可能位置
        
        dp(0)
        return res