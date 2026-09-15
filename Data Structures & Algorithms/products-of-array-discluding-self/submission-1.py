class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        sufix=[1]*len(nums)
        out=[1]*len(nums)
        j=len(nums)-2
        for i in range(1,len(nums)):
            prefix[i]=nums[i-1]*prefix[i-1]
            sufix[j]=nums[j+1]*sufix[j+1]
            j-=1
        for i in range(len(nums)):
            out[i] = prefix[i] * sufix[i]

        return out

        