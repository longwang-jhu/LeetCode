# gradually reduce num and append symbols, include symbols for 900, 400, 90, 40, 9, 4

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        
        res = ""
        for i in range(len(values)):
            while num >= values[i]:
                res += symbols[i]
                num -= values[i]
        
        return res