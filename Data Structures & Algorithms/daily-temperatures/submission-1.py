class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, j = stack[-1]
                result[j] = i - j
                stack.pop()
                    
            stack.append((temp, i))
        return result
        
        