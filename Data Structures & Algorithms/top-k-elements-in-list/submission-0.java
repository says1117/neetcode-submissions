class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int count = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
            if(map.get(nums[i]) > count){
                count = map.get(nums[i]);
            }
        }
        List<Integer>[] buckets = new List[count+1];
        for(int num: map.keySet()){
            int freq = map.get(num);
            if(buckets[freq] == null){
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(num);
        }

        int[] result = new int[k];
        int idx = 0;
        for(int freq = count; freq >=0 && idx < k; freq--){
            if(buckets[freq] != null){
                for(int num: buckets[freq]){
                    if(idx == k) break;
                    result[idx++] = num;
                }
            }
        }
        return result;
    }
}
