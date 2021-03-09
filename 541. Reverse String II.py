# use range(0, n, 2k)

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)