// https://leetcode.com/problems/word-ladder/

// A transformation sequence from word beginWord to word endWord using a dictionary
// wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

// Given two words, beginWord and endWord, and a dictionary wordList, return the
// number of words in the shortest transformation sequence from beginWord to
// endWord, or 0 if no such sequence exists.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> availWords;
        for(auto& word : wordList) availWords.insert(word); availWords.erase(beginWord);
        if (availWords.find(endWord) == availWords.end()) return 0;
        
        queue<string> q; q.push(beginWord);
        int step = 1;
        while (!q.empty()) {
            int nThisLayer = q.size();
            unordered_set<string> usedWordsThisLayer;
            while (nThisLayer--) {
                string thisWord = q.front(); q.pop();
                for (int i = 0; i < thisWord.size(); ++i) { // change every index
                    string nextWord = thisWord;
                    for (int j = 0; j < 26; ++j) { // change word[i] to 'a'--'z'
                        nextWord[i] = 'a' + j;
                        if (nextWord == thisWord) continue;
                        if (nextWord == endWord) return step + 1;
                        if (availWords.find(nextWord) != availWords.end()) { // legal nextWord
                            usedWordsThisLayer.insert(nextWord);
                            q.push(nextWord);
                        }
                    }
                }
            }
            ++step;
            for (auto& word : usedWordsThisLayer) availWords.erase(word);
            usedWordsThisLayer.clear();
        }
        return 0;
    }
};
