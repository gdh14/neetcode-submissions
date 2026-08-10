"""
[()]{}{{}}

{{{]

[]]()

[[[}}

stack = [[[

Intuition:

We can use a stack to store characters. Iterate through the string by index. For an opening bracket, push it onto the stack. If the bracket is a closing type, check for the corresponding opening bracket at the top of the stack. If we don't find the corresponding opening bracket, immediately return false. 

Comment: need to check video solution for a cleaner thought and solution: why the method work? are there easier solutions?

"""

class Solution:
    def isValid(self, s: str) -> bool:
        open_set = set(['[', '{', '('])
        stack = []
        for c in s:
            if c in open_set:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    open_c = stack.pop()
                    if open_c == '[':
                        if c != ']':
                            return False
                    elif open_c == '(':
                        if c != ')':
                            return False
                    elif open_c == '{':
                        if c != '}':
                            return False
                    else:
                        return False
        
        return len(stack) == 0
