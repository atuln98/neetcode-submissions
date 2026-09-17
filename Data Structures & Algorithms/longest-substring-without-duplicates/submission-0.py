class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visi={}
        l=0
        long=0
        for r in range(len(s)):
            while s[r] in visi and visi[s[r]]==1:
                visi[s[l]]=0
                l+=1
            visi[s[r]]=1
            long=max(r-l+1,long)
        return long