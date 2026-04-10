class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c != "+" and c!='-' and c!='*' and c!='/':
                stack.append(int(c))
            elif c == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
            elif c == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
            elif c == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2/num1))
            elif c == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)

        return stack[0]                                





        