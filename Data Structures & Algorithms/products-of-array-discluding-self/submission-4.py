class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        sufix=1
        out=[1]*len(nums)
        j=len(nums)-2
        for i in range(1,len(nums)):
            prefix=nums[i-1]*prefix
            sufix=nums[j+1]*sufix
            out[i]*=prefix
            out[j]*=sufix
            j-=1

        return out

        