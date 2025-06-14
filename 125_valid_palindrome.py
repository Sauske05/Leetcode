'''
This approach checks whether a given string is a valid palindrome, considering only alphanumeric characters and ignoring cases.

Core Logic:
- Use two pointers (`lp` and `rp`) to scan the string from both ends.
- Skip non-alphanumeric characters using `.isalnum()`.
- Compare lowercase versions of characters at `lp` and `rp`.
- If all valid character comparisons match, the string is a palindrome.

--> Time Complexity

Pointer Traversal: Each character in the string is visited at most once by either `lp` or `rp`.

- Skipping non-alphanumeric characters and comparisons are done in constant time per character.

Total Time Complexity: O(n), where n is the length of the input string.

--> Space Complexity

No additional data structures are used other than integer variables.

Total Space Complexity: O(1)
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        lp = 0
        rp = len(s) - 1
        while rp > lp:
            while rp> lp and not s[rp].isalnum():
                rp -=1
            
            while rp > lp and not s[lp].isalnum():
                lp +=1

            if s[rp].lower() == s[lp].lower():
                lp +=1
                rp -=1
            else:
                return False
        return True
            

