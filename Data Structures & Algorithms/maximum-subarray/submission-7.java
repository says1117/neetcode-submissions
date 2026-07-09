class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = -1;
        int n = nums.length;
        int curThread = 0;

        if(n == 1) return nums[0];

        for(int i=0; i<nums.length; i++){

            if(curThread < 0){
                curThread = nums[i];
            }
            else{
                curThread = curThread + nums[i];
            }
            maxSum = Math.max(maxSum, curThread);
        }
        return maxSum;
    }
}
