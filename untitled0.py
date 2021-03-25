# bfs to find the shortest path length
# dfs to get all the pathes

from collections import defaultdict
from collections import deque

def findLadders(beginWord, endWord, wordList):
    # if not beginWord or not endWord or not wordList or endWord not in wordList or beginWord == endWord:
    #     return [], []

    word_len = len(beginWord) # all words have the same length
    next_words_map = defaultdict(set) # key: word, value = list of next words

    queue = deque([beginWord]) # node = (word, path_len)
    words_unused = set(wordList)
    if beginWord in words_unused:
        words_unused.remove(beginWord)
    path_exist = False

    while queue:
        print(queue)
        if endWord in queue: # do not go next layer
            path_exist = True
            break

        used_this_layer = set() # reset at every layer
        curr_len = len(queue)
        for _ in range(curr_len): # scan by layers
            word = queue.popleft()

            for i in range(word_len): # find all child of word
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char != word[i]: # must differ
                        next_word = word[:i] + char + word[i+1:]
                        if next_word in words_unused:
                            next_words_map[word].add(next_word) # add to next_words_map
                            queue.append(next_word) # add to queue
                            used_this_layer.add(next_word)
        words_unused -= used_this_layer

    if not path_exist: return next_words_map, []

    # dfs to find all shortest path
    ans = []
    dfs(ans, [beginWord], endWord, next_words_map)
    return next_words_map, ans

def dfs(ans, holder, endWord, next_words_map):
    if holder[-1] == endWord:
        ans.append(holder.copy())
        return

    word = holder[-1]
    for next_word in next_words_map[word]:
        holder.append(next_word)
        dfs(ans, holder, endWord, next_words_map)
        holder.pop()

beginWord = "lost"
endWord = "cost"
wordList = ["most","fist","lost","cost","fish"]

next_words_map, ans = findLadders(beginWord, endWord, wordList)

print(ans)

