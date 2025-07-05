#from collections import deque
'''
This implementation supports insertion of words, exact word search, and prefix-based search.

--> Time Complexity
- insert(word): O(n), where n is the length of the word
- search(word): O(n), where n is the length of the word
- startsWith(prefix): O(k), where k is the length of the prefix

--> Space Complexity
- O(n * m) in the worst case, where n is the number of inserted words and m is the average word length
- Each node uses a dictionary to store child references, which can grow up to 26 keys in the case of lowercase English letters

Key Details:
- Each `Node` represents a character and maintains a dictionary of child nodes and an `end` flag to mark completion of a word
- The `insert()` method builds the trie by creating new nodes for unseen characters
- The `search()` method returns `True` only if the word exists and ends at a valid word boundary
- The `startsWith()` method checks if a prefix path exists in the trie, regardless of whether it’s a full word

This Trie implementation is efficient for dictionary-like use cases, autocomplete systems, and prefix-based searches.
'''

class Node:
    def __init__(self):

        self.end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.end = True
                

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        if not current.end:
            return False
        else:
            return True


    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)