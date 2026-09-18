class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        monst=[]
        for i in range(len(temperatures)-1,-1,-1):
            pops=0
            while monst and temperatures[i]>=temperatures[monst[-1]]:
                monst.pop()
            if monst:
                pops=monst[-1]-i
            monst.append(i)
            result[i]=pops
        return result