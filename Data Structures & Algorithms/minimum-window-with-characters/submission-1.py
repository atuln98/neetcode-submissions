class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cs={}
        ct={}
        out=""
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
                if len(out)==0:
                    out = s[i:j+1] 
                elif len(out)>len(s[i:j+1]) :
                    out =s[i:j+1]
                if s[i] in ct:
                    cs[s[i]]-=1
                    if cs[s[i]]<ct[s[i]]:
                        have-=1
                i+=1

            j+=1
        return out
        