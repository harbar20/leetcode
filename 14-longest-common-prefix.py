class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def getShortestLength(strings):
            minLen = float('inf')
            for s in strings:
                if len(s) < minLen:
                    minLen = len(s)
                    
            return minLen
        
        if getShortestLength(strs) == 0:
            return ""
        
        if all(len(elem) == len(strs[0]) for elem in strs):
            if all(elem == strs[0] for elem in strs):
                return strs[0]
            else:
                return self.longestCommonPrefix([i[0:-1] for i in strs])
        
        newStrs = list(map(lambda s: s[0: getShortestLength(strs)], strs))
        return self.longestCommonPrefix(newStrs)