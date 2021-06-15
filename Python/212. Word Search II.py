# https://leetcode.com/problems/word-search-ii/

# Given an m x n board of characters and a list of strings words, return all
# words on the board.

# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.

###############################################################################

# Trie: convert words to trie
# bfs: start from every pos on board

from collections import defaultdict
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words: return []
        
        self.board = board
        self.m, self.n = len(board), len(board[0])
        
        # construct a trie
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # search for words
        self.ans = []
        curr = trie.root
        # loop over every pos on board
        for i in range(self.m):
            for j in range(self.n):
                self.holder = []
                self.is_visited = set()
                self.dfs(curr, i, j)
        return self.ans
    
    def dfs(self, curr, i, j):
        if curr.is_word:
            self.ans.append(''.join(self.holder))
            curr.is_word = False
        
        if i < 0 or i == self.m or j < 0 or j == self.n or (i,j) in self.is_visited:
            return
        
        char = self.board[i][j]
        if char not in curr.child:
            return
        else:
            curr = curr.child[char] # move to child
        
        self.holder.append(char)
        self.is_visited.add((i,j))
        
        self.dfs(curr, i - 1, j)
        self.dfs(curr, i + 1, j)
        self.dfs(curr, i, j - 1)
        self.dfs(curr, i, j + 1)
        
        self.holder.pop()
        self.is_visited.remove((i,j))
        
# define TrieNode and Trie
class TrieNode():
    def __init__(self):
        self.child = defaultdict(TrieNode) # key = char, value = TrieNode
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.child[char] # move to child
        curr.is_word = True