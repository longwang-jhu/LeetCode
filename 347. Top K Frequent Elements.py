# https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.

###############################################################################

# number_counter and heapq.nlargest

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.quick_select_top_k(nums, k)
        
        if k == len(nums): return nums
        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=lambda k: counts[k])
    
    def quick_select_top_k(self, nums, k):
        counts = Counter(nums)
        keys = list(counts.keys())

        # find nums.sort()[k:]
        k = len(keys) - k
        self.quick_select(keys, counts, 0, len(keys) - 1, k)
        return keys[k:]
    
    # use quick select to find nums.sort()[k]
    def quick_select(self, keys, counts, start, end, k):
        if start >= end: return
        mid = start + (end - start) // 2
        piv = self.partition(keys, counts, start, end, mid)
        if k == piv:
            return
        elif k < piv:
            self.quick_select(keys, counts, start, piv - 1, k)
        else:
            self.quick_select(keys, counts, piv + 1, end, k)
    
    def partition(self, keys, counts, start, end, piv):
        piv_val = counts[keys[piv]]
        # move piv to end
        keys[piv], keys[end] = keys[end], keys[piv]
        # move all smaller numbers to front
        store_idx = start
        for i in range(start, end):
            if counts[keys[i]] < piv_val:
                keys[store_idx], keys[i] = keys[i], keys[store_idx]
                store_idx += 1
        
        # restore piv
        keys[end], keys[store_idx] = keys[store_idx], keys[end]
        return store_idx