# https://leetcode.com/problems/word-ladder-ii/

# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:

# Given two words, beginWord and endWord, and a dictionary wordList, return all
# the shortest transformation sequences from beginWord to endWord, or an empty
# list if no such sequence exists. Each sequence should be returned as a list
# of the words [beginWord, s1, s2, ..., sk].

###############################################################################

# bfs to find the shortest path length
# dfs to get all the pathes

from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList or endWord not in wordList or beginWord == endWord: 
            return []

        # construct next words dict for dfs
        # key: word, value = list of next words
        next_words_dict = defaultdict(set)

        # construct unused words set, 
        words_avail = set(wordList)
        if beginWord in words_avail: #remove beginWord
            words_avail.remove(beginWord)
        
        # bfs to find the shortest path
        queue = deque([beginWord])
        path_exist = False
        while queue and not path_exist:
            words_used_this_layer = set() # reset at every layer
            for _ in range(len(queue)): # scan by layers
                word = queue.popleft()
                
                found = False # reset for every word
                for i in range(len(word)): # alter every char of word
                    if found: break # stop when one child reach endWord
                    
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        if char != word[i]: # must differ
                            next_word = word[:i] + char + word[i+1:]
                            
                            if next_word in words_avail:
                                queue.append(next_word) # add to queue
                                next_words_dict[word].add(next_word) # add to next_words_dict
                                words_used_this_layer.add(next_word)
                                
                                if next_word == endWord:
                                    found = True
                                    path_exist = True
                                    break # stop generating child for this word

            words_avail -= words_used_this_layer # remove all used word at the end
            
        if not path_exist: return []
        
        # dfs to find all shortest path
        self.ans = []
        self.holder = [beginWord]
        self.endWord = endWord
        self.next_words_dict = next_words_dict
        
        self.dfs()
        return self.ans
    
    def dfs(self):
        if self.holder[-1] == self.endWord: # exit case
            self.ans.append(self.holder.copy())
            return
        
        word = self.holder[-1]
        for next_word in self.next_words_dict[word]:
            self.holder.append(next_word)
            self.dfs()
            self.holder.pop()