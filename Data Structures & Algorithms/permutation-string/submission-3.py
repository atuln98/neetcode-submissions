class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dic={}
        for i in s1:
            if i in s1dic:
                s1dic[i]+=1
            else:
                s1dic[i]=1
        l=0
        s2dic={}
        for r in range(len(s2)):
            s2dic[s2[r]]=s2dic.get(s2[r],0)+1
            if r-l+1>len(s1):
                s2dic[s2[l]]-=1
                if s2dic[s2[l]]==0:
                    del s2dic[s2[l]]
                l+=1
            if r-l+1==len(s1) and s1dic==s2dic:
                return True
        return False
        