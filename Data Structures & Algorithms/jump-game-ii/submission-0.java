class Solution {
    public int jump(int[] nums) {
        int feasible = 0;
        int best = 0;
        int amt = 0;

        for(int i=0; i<nums.length-1; i++){
            feasible = Math.max(feasible, i+nums[i]);

            if(i==best){
                amt++;
                best = feasible;
            }
        }
        return amt;
    }
}
