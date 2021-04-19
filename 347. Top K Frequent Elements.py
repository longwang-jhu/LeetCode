# https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.

###############################################################################

# number_counter and heapq.nlargest

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.top_k_qs(nums, k)
        
        if k == len(nums): return nums
        
        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=lambda k: counts[k])
    
    def top_k_qs(self, nums, k): # use quick select to find top k
        counts = Counter(nums)
        keys = list(counts.keys())
        
        def partition(left, right, piv):
            piv_val = counts[keys[piv]]
            # move piv to right
            keys[piv], keys[right] = keys[right], keys[piv]
            # move all smaller numbers to left
            store_idx = left
            for i in range(left, right):
                if counts[keys[i]] < piv_val:
                    keys[store_idx], keys[i] = keys[i], keys[store_idx]
                    store_idx += 1
            # move piv
            keys[right], keys[store_idx] = keys[store_idx], keys[right]
            
            return store_idx
        
        def quick_select(left, right, k):
            if left == right: return
            
            piv = random.randint(left, right)
            piv = partition(left, right, piv)
            if k == piv:
                return
            elif k < piv: # go left
                quick_select(left, piv - 1, k)
            else:
                quick_select(piv + 1, right, k)
        
        n = len(keys)
        quick_select(0, n - 1, n - k)
        return keys[n - k:]
            
            
            
            
            