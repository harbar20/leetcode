class Solution:
    def __init__(self):
        thing = 0
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        encountered = []
        for c in s:
            maxSoFar = len(encountered)
            
            if c not in encountered:
                encountered.append(c)
            else:
                nextMax = self.lengthOfLongestSubstring(s[1:])
                if maxSoFar > nextMax:
                    return maxSoFar
                return nextMax
        
        return len(encountered)

def test(string: str, exp: int):
    sol = Solution()
    res = sol.lengthOfLongestSubstring(string)
    assert res == exp, f"Is {res}, should be {exp}"
    
def tests():
    test("abcabcbb", 3)
    test("bbbbb", 1)
    test("pwwkew", 3)
    test("au", 2)
    test("aab", 2)
    test("dvdf", 3)
    print("All tests passed!")
    
tests()