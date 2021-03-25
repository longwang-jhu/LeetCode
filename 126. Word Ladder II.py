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

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList or endWord not in wordList or beginWord == endWord: 
            return []
        
        word_len = len(beginWord) # all words have the same length
        next_words_map = collections.defaultdict(set) # key: word, value = list of next words
        
        queue = collections.deque([beginWord])
        words_unused = set(wordList)
        if beginWord in words_unused:
            words_unused.remove(beginWord)
        path_exist = False
        
        while queue and not path_exist: # scan by layers
            used_this_layer = set() # reset at every layer
            curr_layer_len = len(queue)
            for _ in range(curr_layer_len):
                word = queue.popleft()
                
                next_is_end = False
                for i in range(word_len): # find all child of word
                    if next_is_end:
                        break # stop generating child for this word
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        if char != word[i]: # must differ
                            next_word = word[:i] + char + word[i+1:]
                            
                            if next_word in words_unused:
                                next_words_map[word].add(next_word) # add to next_words_map
                                queue.append(next_word) # add to queue
                                used_this_layer.add(next_word)
                                
                                if next_word == endWord:
                                    next_is_end = True
                                    path_exist = True
                                    break # stop generating child for this word
                                
            words_unused -= used_this_layer # remove all used word at the end
            
        if not path_exist: return []
        
        # dfs to find all shortest path
        ans = []
        self.dfs(ans, [beginWord], endWord, next_words_map)
        return ans
    
    def dfs(self, ans, holder, endWord, next_words_map):
        if holder[-1] == endWord:
            ans.append(holder.copy())
            return
        
        word = holder[-1]
        for next_word in next_words_map[word]:
            holder.append(next_word)
            self.dfs(ans, holder, endWord, next_words_map)
            holder.pop()
