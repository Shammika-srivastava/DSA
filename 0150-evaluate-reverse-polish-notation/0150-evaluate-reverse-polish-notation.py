class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num == '+':
                stack.append(stack.pop() + stack.pop())
            elif num == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif num == '*':
                stack.append(stack.pop() * stack.pop())
            elif num == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))  # truncate toward 0 i.e -2.333= -2 not -3
            else:
                stack.append(int(num))
        return stack[0]
