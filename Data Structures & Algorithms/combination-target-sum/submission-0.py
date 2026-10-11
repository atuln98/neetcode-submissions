class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solutions=[]

        def backtrack(target,currset,currindex):
            if target==0:
                solutions.append(currset.copy())
                return
            for i in nums[currindex:]:
                if i<=target:
                    currset.append(i)
                    backtrack(target-i,currset,currindex)
                    currset.pop()
                currindex+=1
            return

        backtrack(target,[],0)
        return solutions
        