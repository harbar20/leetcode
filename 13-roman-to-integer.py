class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        if s == "":
            return 0
        
        maxIndex = 0
        for i in range(len(s)):
            numeral = s[i]
            if values[numeral] > values[s[maxIndex]]:
                maxIndex = i
        
        return values[s[maxIndex]] - self.romanToInt(s[0:maxIndex]) + self.romanToInt(s[maxIndex+1:])