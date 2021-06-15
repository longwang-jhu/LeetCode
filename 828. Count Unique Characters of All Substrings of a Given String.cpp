// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

// Let's define a function countUniqueChars(s) that returns the number of unique
// characters on s, for example if s = "LEETCODE" then "L", "T","C","O","D" are the
// unique characters since they appear only once in s, therefore
// countUniqueChars(s) = 5.

// On this problem given a string s we need to return the sum of
// countUniqueChars(t) where t is a substring of s. Notice that some substrings can
// be repeated so on this case you have to count the repeated ones too.

// Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.

////////////////////////////////////////////////////////////////////////////////

// for each char, find all substrings where it will be counted as unique char
// for eaach s[i] its prevOccurIdx l and nextOccurIdx r [...A|...A...|A...]
// number of substrings = (i - l) * (r - i)
class Solution {
public:
    int uniqueLetterString(string s) {
        const int MOD = 1e9 + 7;
        int n = s.size();
        unordered_map<char, vector<int>> occurIdxes;
        for (int i = 0; i < n; ++i) {
            if (occurIdxes.find(s[i]) == occurIdxes.end()) occurIdxes[s[i]].push_back(-1);
            occurIdxes[s[i]].push_back(i);
        }
        for (auto& [key, idxes] : occurIdxes) {
            idxes.push_back(n);
        }
        
        long int ans = 0;
        for (auto& [key, idxes] : occurIdxes) {
            for (int i = 1; i < idxes.size() - 1; ++i) {
                ans = (ans + (long int) (idxes[i] - idxes[i-1]) * (idxes[i+1] - idxes[i]) % MOD) % MOD;
            }
        }
        return (int) ans;
    }
};
