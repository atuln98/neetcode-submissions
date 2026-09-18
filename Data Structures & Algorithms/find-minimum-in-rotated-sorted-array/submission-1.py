class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        mine=nums[0]
        while(l<r):
            mine=min(nums[l],nums[r])
            if(nums[(l+r)//2]>nums[r]):
                l=(l+r)//2+1
            else:
                r=(l+r)//2
        return mine