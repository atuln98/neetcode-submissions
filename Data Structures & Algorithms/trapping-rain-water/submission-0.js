class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let l_max=0
        let r_max=0
        let l=0
        let water=0
        let r=height.length-1
        while(l<r){
            if(height[l]<height[r]){
                l_max=Math.max(height[l],l_max)
                water+=l_max-height[l]
                l+=1
            }else{
                r_max=Math.max(height[r],r_max)
                water+=r_max-height[r]
                r-=1
            }
        }
        return water
    }
}
