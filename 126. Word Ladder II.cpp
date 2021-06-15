// https://leetcode.com/problems/word-ladder-ii/

// A transformation sequence from word beginWord to word endWord using a dictionary
// wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

// Given two words, beginWord and endWord, and a dictionary wordList, return all
// the shortest transformation sequences from beginWord to endWord, or an empty
// list if no such sequence exists. Each sequence should be returned as a list of
// the words [beginWord, s1, s2, ..., sk].

////////////////////////////////////////////////////////////////////////////////

// bfs to find length, dfs to find all sequences
class Solution {
public:
    vector<vector<string>> ans;
    vector<string> holder;
    
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> availWords;
        for (string& word : wordList) availWords.insert(word); availWords.erase(beginWord);
        if (availWords.find(endWord) == availWords.end()) return {};
        
        // nextWords[word] = set of next words, useful for dfs
        unordered_map<string, unordered_set<string>> nextWords;
        queue<string> todo; todo.push(beginWord);
        bool foundByThisLayer = false;
        while(!todo.empty() and !foundByThisLayer) {
            int nThisLayer = todo.size();
            unordered_set<string> usedWordsThisLayer;
            while (nThisLayer--) {
                string thisWord = todo.front(); todo.pop();
                bool foundByThisWord = false; // for early stopping
                for (int i = 0; i < thisWord.size(); ++i) { // change every index
                    if (foundByThisWord) break;
                    string nextWord = thisWord; 
                    for (int j = 0; j < 26; ++j) { // change word[i] to 'a'--'z'
                        nextWord[i] = 'a' + j;
                        if (nextWord == thisWord) continue;
                        if (availWords.find(nextWord) != availWords.end()) { // legal word
                            usedWordsThisLayer.insert(nextWord);
                            nextWords[thisWord].insert(nextWord);
                            todo.push(nextWord);
                            if (nextWord == endWord) { 
                                foundByThisWord = true; foundByThisLayer = true; break;
                            }
                        }
                    }
                }
            }
            // remove used words from availWords
            for (string word : usedWordsThisLayer) availWords.erase(word);
        }
        if (!foundByThisLayer) return {};
        // dfs to find all paths
        holder.push_back(beginWord);
        dfs(endWord, nextWords);
        return ans;
    }
    
    void dfs(const string& endWord, unordered_map<string, unordered_set<string>>& nextWords) {
        if (holder.back() == endWord) {
            ans.push_back(holder); return;
        }
        string thisWord = holder.back();
        for (auto &nextWord : nextWords[thisWord]) {
            holder.push_back(nextWord);
            dfs(endWord, nextWords);
            holder.pop_back();
        }
        return;
    }
};
