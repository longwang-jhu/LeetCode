# use dict with key = min(d[0], d[1]) * 10 + max(d[0], d[1])

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_dict = {}
        for d in dominoes:
            key = min(d[0], d[1]) * 10 + max(d[0], d[1])
            if key in domino_dict:
                domino_dict[key] += 1
            else:
                domino_dict[key] = 1
        
        ans = 0
        for value in domino_dict.values():
            ans += value * (value - 1) / 2
        
        return int(ans)