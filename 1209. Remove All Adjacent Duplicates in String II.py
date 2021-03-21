# use stack and record the count
# use dummy element ('#', 0)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]] # dummy element
        
        for char in s:
            if stack[-1][0] == char: # duplicate
                stack[-1][1] += 1 # increment count
                if stack[-1][1] == k:
                    stack.pop() # remove the duplicate
            else: # no duplicate
                stack.append([char, 1])

        return ''.join(char * count for char, count in stack)