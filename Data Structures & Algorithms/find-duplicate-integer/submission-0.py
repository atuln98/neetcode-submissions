class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow=nums[slow]
            fast = nums[nums[fast]]
            if nums[slow]==nums[fast]:
                break
        follow = 0
        while True:
            follow=nums[follow]
            slow=nums[slow]
            if follow==slow:
                return slow
        