class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lefts = set()
        lefts.add("(")
        lefts.add("{")
        lefts.add("[")
        for char in s:
            if char in lefts:
                stack.append(char)
            else:
                if char == ")":
                    if stack and stack[-1] == "(":
                        del stack[-1]
                    else:
                        return False
                elif char == "}":
                    if stack and stack[-1] == "{":
                        del stack[-1]
                    else:
                        return False
                elif char == "]":
                    if stack and stack[-1] == "[":
                        del stack[-1]
                    else:
                        return False
        
        if not stack:
            return True
        else:
            return False
                

        