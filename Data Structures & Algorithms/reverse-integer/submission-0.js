class Solution {
    /**
     * @param {number} x
     * @return {number}
     */
    reverse(x) {
            let out=0
            while(x!==0){
                out=out*10+(x%10)
                x=Math.trunc(x/10)
            }
        if(out<-(2**31) || out> (2**31)-1){
            return 0
        }
            return out
    }

}
