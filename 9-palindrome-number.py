import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
        def numDigits(y: int):
            return int(math.log10(y))+1 # Credit to John La Rooy on StackOverflow
        
        def isPalindromeHelper(y: int):
            if y < 0:
                return False
            
            if y < 10:
                return True
            
            digits = numDigits(y)
            
            firstDigit = y // pow(10,digits-1)
            middleDigits = (y - (firstDigit * pow(10, digits-1))) // 10
            lastDigit = y % 10
            
            return (firstDigit == lastDigit) and isPalindromeHelper(middleDigits)
        
        return isPalindromeHelper(x)