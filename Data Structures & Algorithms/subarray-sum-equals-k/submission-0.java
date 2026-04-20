class Solution {
    public int subarraySum(int[] nums, int k) {
        int n=nums.length;
        Map<Integer,Integer> m=new HashMap<>();
        m.put(0,1);
        for(int i=1;i<n;i++){
            nums[i]=nums[i]+nums[i-1];
        }
        int count=0;
        for(int i=0;i<n;i++){
            int res=nums[i]-k;
            if(m.containsKey(res)){
                count+=m.get(res);
            }
            int val=m.getOrDefault(nums[i],0)+1;
            m.put(nums[i],val);
        }
        return count;
    }
}