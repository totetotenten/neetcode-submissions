class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        path = []
        for token in tokens:
            if token in operators:
                prev_1, prev_2 = path[-2], path[-1]
                if token == "+":
                    tmp = prev_1 + prev_2
                elif token == "-":
                    tmp = prev_1 - prev_2
                elif token == "*":
                    tmp = prev_1 * prev_2
                elif token == "/":
                    tmp = int(prev_1 / prev_2)
                path.pop()
                path.pop()

            else:
                tmp = int(token)
            path.append(tmp)
        return path[0] 