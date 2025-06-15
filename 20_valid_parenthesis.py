'''
This approach validates a string containing parentheses by using a stack to ensure that every opening bracket has a matching and correctly placed closing bracket.

--> Logic

1. A dictionary `p_map` maps each opening bracket to its corresponding closing bracket.
2. Iterate through each character in the string `s`.
   - If it's an opening bracket, push it onto the stack.
   - If it's a closing bracket:
     - Check if the stack is empty. If yes, it means there's no matching opening bracket, so return False.
     - Pop the top of the stack and check if it maps correctly to the current closing bracket. If not, return False.
3. After the loop, if the stack is not empty, it means there are unmatched opening brackets, so return False. Otherwise, return True.

--> Time Complexity

- Iteration through `s`: O(n), where n is the length of the string.
- Stack operations (push and pop): O(1) each, done at most n times.

Total Time Complexity: O(n)

--> Space Complexity

- Stack: In the worst case, all characters are opening brackets, so the stack could hold up to n elements.

Total Space Complexity: O(n)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []

        if len(s) < 2:
            return False

        for p in s:
            if p in p_map:
                stack.append(p)

            else:
                if not stack:
                    return False
                last_element = stack.pop()
                if p_map[last_element] != p:
                    return False

        return True if not stack else False