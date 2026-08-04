class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                    del stack[-1]
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack

        