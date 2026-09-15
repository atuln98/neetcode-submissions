class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ha={}
        for i in range(0,len(nums)):
            ha[nums[i]]=i
        for i in range(0,len(nums)):
            find=target-nums[i]
            if find in ha:
                if ha[find] == i:
                    continue
                return [i,ha[find]]
        return[]