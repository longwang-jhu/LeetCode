# https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Design a data structure that supports adding new words and finding if a string
# matches any previously added string.

# Implement the WordDictionary class:

################################################################################

from collections import defaultdict
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, 0, word)
    
    def dfs(self, node, idx, word):
        if idx == len(word): return node.is_word
        
        char = word[idx]
        if char == ".":
            for child in node.children:
                if self.dfs(node.children[child], idx + 1, word):
                    return True
        else:
            if char not in node.children:
                return False
            else:
                return self.dfs(node.children[char], idx + 1, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
