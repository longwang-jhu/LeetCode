# https://leetcode.com/problems/word-ladder/

# A transformation sequence from word beginWord to word endWord using a dictionary
# wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Given two words, beginWord and endWord, and a dictionary wordList, return the
# number of words in the shortest transformation sequence from beginWord to
# endWord, or 0 if no such sequence exists.

################################################################################

# shortest pass from beginWord to endWord
# bfs with queue
# define node = (word, path_len)
# generate children by altering every char in word and make sure next word is in wordList

# use set(wordList) for O(1) lookup time
# word in wordList should be used just once

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words_set = set(wordList) # for O(1) lookup time
        
        queue = collections.deque([(beginWord, 1)]) # (word, path_len)
        while queue:
            word, path_len = queue.popleft()
            if word == endWord:
                return path_len
            
            for i in range(len(word)): # generated child by alter chars in word
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char != word[i]: # must differ
                        word_next = word[:i] + char + word[i+1:] # alter word[i]
                        if word_next in words_set:
                            words_set.remove(word_next) # use only once
                            queue.append((word_next, path_len + 1))
        return 0
