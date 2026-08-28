class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                j = stack[-1][1]
                result[j] = i - j
                del stack[-1]
                    
            stack.append([temp, i])
        return result
        