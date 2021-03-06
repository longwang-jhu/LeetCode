# check if B is a substring of A + A
# O(n^2): use B in A + A

# O(n): rolling Hash
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A