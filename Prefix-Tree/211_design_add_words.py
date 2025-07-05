# Implementation of a Trie-based Word Dictionary with support for wildcard search ('.')

'''
This approach builds a Trie to store words and allows searching with support for the wildcard character `.`.

--> Time Complexity
- addWord(word): O(n), where n is the length of the word
- search(word): Worst case O(m^n), where:
    - m is the average branching factor (number of children per node)
    - n is the length of the word
    - This happens when multiple `.` wildcards force branching into many paths

--> Space Complexity
- O(n * k), where n is the number of words and k is the average word length
- Each TrieNode uses a dictionary to store child nodes

Key Details:
- `TrieNode` contains a `children` dictionary and an `is_end` flag
- `addWord()` adds words to the trie character by character
- `search()` uses DFS to explore paths, supporting `.` which can match any character
    - If a `.` is encountered, all child nodes are recursively searched
    - Otherwise, the specific character path is followed

This design is efficient for word lookup and flexible for pattern-based queries using wildcard characters.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.is_end
            ch = word[index]
            if ch == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])
        
        return dfs(0, self.root)
