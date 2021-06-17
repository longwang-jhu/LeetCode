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
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> availWords;
        for (const string& word : wordList) availWords.insert(word);
        availWords.erase(beginWord);
        if (availWords.find(endWord) == availWords.end()) return {};
        
        queue<string> todo; todo.push(beginWord);
        bool found = false;
        while(!todo.empty() and !found) {
            int nCurrLayer = todo.size();
            unordered_set<string> usedWordsCurrLayer;
            while (nCurrLayer--) {
                string currWord = todo.front(); todo.pop();
                bool foundByCurrWord = false; // for early stopping
                for (int i = 0; i < currWord.size(); ++i) { // change every index
                    if (foundByCurrWord) break;
                    string nextWord = currWord;
                    for (int j = 0; j < 26; ++j) { // change currWord[i] to 'a'--'z'
                        nextWord[i] = 'a' + j;
                        if (nextWord[i] == currWord[i]) continue;
                        if (availWords.find(nextWord) != availWords.end()) { // legal child
                            usedWordsCurrLayer.insert(nextWord);
                            wordsMap[currWord].insert(nextWord); // add to wordsMap
                            todo.push(nextWord);
                            if (nextWord == endWord) { 
                                foundByCurrWord = true; found = true;
                                break;
                            }
                        }
                    }
                }
            }
            // remove used words from availWords
            for (const string& word : usedWordsCurrLayer) availWords.erase(word);
        }
        if (!found) return {};
        // dfs to find all paths
        holder.push_back(beginWord);
        dfs(endWord);
        return ans;
    }
private:
    // wordsMap[word] = set of next words, useful for dfs
    unordered_map<string, unordered_set<string>> wordsMap;
    vector<string> holder;
    vector<vector<string>> ans;
    void dfs(const string& endWord) {
        if (holder.back() == endWord) {
            ans.push_back(holder); return;
        }
        string currWord = holder.back();
        for (const auto& nextWord : wordsMap[currWord]) {
            holder.push_back(nextWord);
            dfs(endWord);
            holder.pop_back();
        }
        return;
    }
};
