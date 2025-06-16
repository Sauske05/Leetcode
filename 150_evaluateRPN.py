from typing import List
'''
This approach evaluates a Reverse Polish Notation (postfix) expression using a stack.

Key Idea:
- Traverse the list of tokens.
- Push operands (numbers) onto the stack.
- When an operator is encountered, pop the last two operands, apply the operation, and push the result back.
- Repeat until all tokens are processed. The last element in the stack is the result.

Special Note:
- For division, Python’s int() is used after floating point division to truncate towards zero as specified by the problem (not floor division like // for negatives).

--> Time Complexity

Each token is processed exactly once in a loop of size n:
- For operands: pushed to stack → O(1)
- For operators: pop two, compute, push → O(1)

Total Time Complexity: O(n), where n is the number of tokens

--> Space Complexity

Stack stores at most n/2 numbers (in worst case all are operands, except operators being few).

Total Space Complexity: O(n)
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(a+ b)
                elif token == '-':
                    stack.append(b-a)
                elif token == '*':
                    stack.append(a* b)
                elif token == '/':
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[-1]