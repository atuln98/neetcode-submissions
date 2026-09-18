from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while(low<high):
            k=(low + high)//2
            currh=0
            for i in piles:
                currh+=ceil(i/k)
                if currh>h:
                    low=k+1
                    break
            if currh<=h:
                    high=k
        return low