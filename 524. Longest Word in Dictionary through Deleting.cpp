// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

// Given a string s and a string array dictionary, return the longest string in the
// dictionary that can be formed by deleting some of the given string characters.
// If there is more than one possible result, return the longest word with the
// smallest lexicographical order. If there is no possible result, return the empty
// string.

////////////////////////////////////////////////////////////////////////////////

// sort dictionary and check every key
class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        sort(dictionary.begin(), dictionary.end(), [](string& a, string& b) {
            return (a.size() == b.size()) ? (a < b) : (a.size() > b.size());
        });
        
        for (auto &key : dictionary) {
            if (isSubstr(s, key)) return key;
        }
        return {};
    }
    
    // check if key is substr of s
    bool isSubstr(string& s, string& key) {
        int i = 0, j = 0;
        while (i < s.size() and j < key.size()) {
            if (s[i] == key[j]) ++j;
            ++i;
        }
        return j == key.size();
    }
};
