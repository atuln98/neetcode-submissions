class Solution:

    def encode(self, strs: List[str]) -> str:
        out=""
        for i in strs:
            out+=str(len(i))+"#"+i
        return out


    def decode(self, s: str) -> List[str]:
        out=[]
        curr=0
        i=0
        while i<len(s):
            if s[i] == "#":
                length = int(s[curr:i])
                out.append(s[i+1:i+length+1])
                curr=i=i+length+1
            else:
                i+=1
        return out