class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r=0
        l=len(heights)-1
        out=0
        while r<l:
            area=(l-r)*min(heights[r],heights[l])
            if heights[r]>heights[l]:
                l-=1
            else:
                r+=1
            out=max(out,area)
        return out
        
        