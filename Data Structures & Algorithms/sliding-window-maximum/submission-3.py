class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        track=[]
        out=[]
        i=0
        while i<len(nums):
            if track and track[0]<=i-k:
                track.pop(0)
            while track and nums[track[-1]] < nums[i]:
                track.pop(len(track)-1)
            track.append(i)  
            if i >= k-1:
                out.append(nums[track[0]])          
            i+=1
        return out
