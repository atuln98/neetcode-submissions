class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visi={}
        l=0
        long=0
        for r in range(len(s)):
            if s[r] in visi and visi[s[r]]>=l:
                l=visi[s[r]]+1
            else:
                long=max(r-l+1,long)
            visi[s[r]]=r
        return long