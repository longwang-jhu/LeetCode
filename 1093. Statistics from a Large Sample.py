# https://leetcode.com/problems/statistics-from-a-large-sample/

# You are given a large sample of integers in the range [0, 255]. Since the sample
# is so large, it is represented by an array count where count[k] is the number of
# times that k appears in the sample.

# Calculate the following statistics:

# Return the statistics of the sample as an array of floating-point numbers
# [minimum, maximum, mean, median, mode]. Answers within 10-5 of the actual answer
# will be accepted.

################################################################################

# basic counting

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = sum(count)
        
        # get minimum
        for i in range(256):
            if count[i] != 0:
                minimum = i
                break
        
        # get maximum
        for i in range(255, -1, -1):
            if count[i] != 0:
                maximum = i
                break
        
        # get mean
        mean = 0
        for i in range(256):
            mean += i * count[i] / n
        
        # get median
        # find (n + 1) // 2
        cum_count, i = 0, -1
        while cum_count < (n + 1) // 2:
            i += 1
            cum_count += count[i]
        median = i
        
        if n % 2 == 0: # if even find (n + 2) // 2
            while cum_count < (n + 2) //2:
                i += 1
                cum_count += count[i]
            median = (median + i) / 2
        
        # get mode
        max_count = max(count)
        for i in range(256):
            if count[i] == max_count:
                mode = i
                break
        
        return [minimum, maximum, mean, median, mode]
