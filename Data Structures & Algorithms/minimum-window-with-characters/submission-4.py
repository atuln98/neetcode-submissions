class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t== "" or len(t)>len(s):
            return ""
        cs={}
        ct={}
        out=0
        besti=0
        bestj=0
        have = 0
        for i in t:
            ct[i]=ct.get(i,0)+1
        i=j=0
        need = len(ct)
        while j<len(s):
            if s[j] in ct:
                cs[s[j]]=cs.get(s[j],0)+1
                if cs[s[j]]==ct[s[j]]:
                    have+=1
            while have == need:
                if out==0:
                    out = j-i+1
                    besti=i
                    bestj=j
                elif out>j-i+1:
                    out = j-i+1
                    besti=i
                    bestj=j
                if s[i] in ct:
                    cs[s[i]]-=1
                    if cs[s[i]]<ct[s[i]]:
                        have-=1
                i+=1

            j+=1
        if out==0:
            return ""
        return s[besti:bestj+1]
        