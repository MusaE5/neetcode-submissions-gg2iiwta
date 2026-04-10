class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    sum = left + right
                elif token == "-":
                    sum = left-right
                elif token == "*":
                    sum = left*right
                elif token == "/":
                    sum = int(left/right)    

                stack.append(sum)

        return stack[0]        



       

