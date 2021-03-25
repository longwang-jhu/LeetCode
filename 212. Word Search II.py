# https://leetcode.com/problems/word-search-ii/

# Given an m x n board of characters and a list of strings words, return all
# words on the board.

# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.

###############################################################################

# Trie: convert words to trie
# bfs: start from every position on board

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words: return []
        
        m, n = len(board), len(board[0])
        
        # construct a trie
        trie = Trie()
        curr = trie.root
        for word in words:
            trie.insert(word)
        
        # search for words
        visited = [[False] * n for _ in range(m)]
        ans = []
        
        for i in range(m):
            for j in range(n):
                self.dfs(ans, [], curr, i, j, board, visited)
        return ans
    
    def dfs(self, ans, holder, curr, i, j, board, visited):
        if curr.is_word:
            ans.append(''.join(holder))
            curr.is_word = False
        
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited[i][j]:
            return
        
        if board[i][j] not in curr.children:
            return
        else:
            curr = curr.children[board[i][j]] # move to child
        
        holder.append(board[i][j])
        visited[i][j] = True
        
        self.dfs(ans, holder, curr, i - 1, j, board, visited)
        self.dfs(ans, holder, curr, i + 1, j, board, visited)
        self.dfs(ans, holder, curr, i, j - 1, board, visited)
        self.dfs(ans, holder, curr, i, j + 1, board, visited)
        
        holder.pop()
        visited[i][j] = False
        
# define TrieNode and Trie
class TrieNode():
    def __init__(self):
        self.children = dict() # key = char, value = TrieNode
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char] # move to child
        curr.is_word = True