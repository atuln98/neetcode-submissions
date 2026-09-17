class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        cdict={}
        maxfreq=0
        maxwindow=0
        for i in range(0,len(s)):
            if s[i] in cdict:
                cdict[s[i]]+=1
            else:
                cdict[s[i]]=1
            maxfreq=max(maxfreq,cdict[s[i]])
            if i-left+1-maxfreq>k:
                cdict[s[left]]-=1
                left+=1
            else:
                maxwindow=max(i-left+1,maxwindow)
        return maxwindow
        