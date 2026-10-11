class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions=[]
        nums=sorted(candidates)
        def backtrack(target,currset,currindex):
            if target==0:
                solutions.append(currset.copy())
                return
            skip = 0
            for i in nums[currindex:]:
                if skip:
                    skip=0
                    if currindex<len(nums) and nums[currindex] == prev:
                        skip=1
                        currindex+=1
                    continue
                if i<=target:
                    currset.append(i)
                    backtrack(target-i,currset,currindex+1)
                    prev=currset.pop()
                    if currindex+1<len(nums) and nums[currindex+1] == prev:
                        skip=1
                        currindex+=1
                currindex+=1
            return

        backtrack(target,[],0)
        return solutions
        