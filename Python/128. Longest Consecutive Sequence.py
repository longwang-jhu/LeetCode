# use set
# look for num that (num - 1) is not in the set
# start from that num and look for consecutive sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        
        for num in nums_set:
            if num - 1 not in nums_set: # find num that cannot go lower
                curr_num = num
                curr_len = 1
                
                while curr_num + 1 in nums_set: # build seq from curr_num
                    curr_num += 1
                    curr_len += 1
                
                max_len = max(max_len, curr_len)
        
        return max_len