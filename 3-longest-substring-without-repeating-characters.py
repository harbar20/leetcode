class Solution:
    def __init__(self):
        thing = 0
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        finalStr = ""
        continuous = []
        for c in s:
            if c not in finalStr:
                finalStr += c
            else:
                continuous.append(len(finalStr))
                finalStr = c
            #print(finalStr)
                
        #print(continuous)
        continuous.append(len(finalStr))
        return max([1, max(continuous or [0])])

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb")) # 3
print("-------------")
print(sol.lengthOfLongestSubstring("bbbbb"))    # 1
print("-------------")
print(sol.lengthOfLongestSubstring("pwwkew"))   # 3
print("-------------")
print(sol.lengthOfLongestSubstring("au"))   # 2
print("-------------")
print(sol.lengthOfLongestSubstring("aab"))   # 2
print("-------------")