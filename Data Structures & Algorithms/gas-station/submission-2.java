class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalGas = 0;
        int mostIdx = 0;

        if(Arrays.stream(gas).sum() < Arrays.stream(cost).sum()) return -1;

        for(int i=0; i < gas.length; i++){
            totalGas += gas[i] - cost[i];
            if(totalGas < 0){
                totalGas = 0;
                mostIdx = i+1;
            }
        }
        return mostIdx;
    }
}
