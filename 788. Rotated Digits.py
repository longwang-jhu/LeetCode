# loop over all numbers

class Solution:
    def rotatedDigits(self, N: int) -> int:
        def is_valid(num):
            valid_flag = False
            while num > 0:
                last_digit = num % 10
                if last_digit in [3, 4, 7]:
                    return False
                elif last_digit in [2, 5, 6, 9]:
                    valid_flag = True
                num = num // 10
            return valid_flag

        ans = 0
        for num in range(1, N + 1):
            if is_valid(num):
                ans += 1
        return ans