# https://leetcode.com/problems/binary-watch/

# A binary watch has 4 LEDs on the top which represent the hours (0-11), and
# the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a
# zero or one, with the least significant bit on the right.

# 

# Given an integer turnedOn which represents the number of LEDs that are
# currently on, return all possible times the watch could represent. You may
# return the answer in any order.

# The hour must not contain a leading zero.

# The minute must be consist of two digits and may contain a leading zero.

###############################################################################

# use bin(i).count("1") to find
# hour[idx] = hours with no. of lights == idx
# minute[idx] = minute with no. of lights == idx

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        hour = [[], [], [], []]
        minute = [[], [], [], [], [], []]
        
        for i in range(12):
            light_count = bin(i).count("1")
            hour[light_count].append(i)
        for i in range(60):
            light_count = bin(i).count("1")
            minute[light_count].append(i)
        
        for i in range(turnedOn + 1):
            hour_light = i
            minute_light = turnedOn - i
            
            if hour_light < 4 and minute_light < 6:
                for h in hour[hour_light]:
                    for m in minute[minute_light]:
                        ans.append('%d:%02d' % (h, m))
        return ans