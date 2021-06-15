// https://leetcode.com/problems/implement-strstr/

// Implement strStr().

// Return the index of the first occurrence of needle in haystack, or -1 if needle
// is not part of haystack.

// Clarification:

// What should we return when needle is an empty string? This is a great question
// to ask during an interview.

// For the purpose of this problem, we will return 0 when needle is an empty
// string. This is consistent to C's strstr() and Java's indexOf().

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.size() == 0) return 0;
        if (haystack.size() == 0) return -1;
        
        for (size_t i = 0; i + needle.size() - 1 < haystack.size(); ++i) {
            if (haystack.substr(i, needle.size()) == needle) return i;
        }
        return -1;   
    }
};
