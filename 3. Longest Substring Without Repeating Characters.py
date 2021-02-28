# use charDict[char] = idx
# reset startIdx if necessary
# keep updating maxLen

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        maxLen = 0
        startIdx = 0
        for idx, char in enumerate(s):
            if char in charDict:
                prevCharIdx = charDict[char]
                if prevCharIdx + 1 > startIdx: # reset startIdx if necessary
                    # set the start idx to the right of the repeated char
                    startIdx = prevCharIdx + 1

            # update maxLen
            currLen = idx - startIdx + 1
            maxLen = max(currLen, maxLen)

            # save char into charDict
            charDict[char] = idx

        return maxLen