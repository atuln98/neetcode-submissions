class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        let out=[]

        function backtrack(start,remain){
            if (remain.length==0){
                out.push([...start])
            }
            const tried={}
            for (let i=0;i<remain.length;i++){
                if  (tried[remain[i]]){
                    continue
                } 
                tried[remain[i]] = true
                start.push(remain[i])
                backtrack(start,remain.slice(0,i).concat(remain.slice(i+1)))
                start.pop()
            }
        }
        backtrack([],nums)
        return out
    }
}
