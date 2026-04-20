class Solution {
    public int[] sortArray(int[] nums) {
        PriorityQueue<Integer> pq=new PriorityQueue<>();
        for(int i=0;i<nums.length;i++){
            pq.offer(nums[i]);
            nums[i]=0;
        }
        int i=0;
        while(!pq.isEmpty()){
            nums[i++]=pq.poll();
        }
        return nums;
    
    }
}