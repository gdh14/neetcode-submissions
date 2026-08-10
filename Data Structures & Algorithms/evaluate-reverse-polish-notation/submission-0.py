""" 
Intuition: maintain a stack to keep track of tokens. 
- digit: append to stack
- operator: pop the two digit from stack, and append result

Acutually simple as long as I know how RPN works.

[4,5]-
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a) # watch out for the order [b, a] - => b - a
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a)) # use int to "truncates toward zero"
            else:
                stack.append(int(c))
        
        return stack[0]


        