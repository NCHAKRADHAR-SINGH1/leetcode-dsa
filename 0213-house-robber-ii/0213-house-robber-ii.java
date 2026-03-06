class Solution {
    public int rob(int[] nums) {
       if(nums.length==1) return nums[0];
       int n=nums.length;
       int max1=robHelp(nums,0,n-2);
       int max2=robHelp(nums,1,n-1);
       return Math.max(max1,max2);
    }
      public int robHelp(int[] nums,int start,int end){
            int size=end-start+1;
            int dp[]=new int[size];
            dp[0]=nums[start];
            if(size > 1){
               dp[1]=Math.max(nums[start],nums[start+1]);
            }
            for(int i=2;i<size;i++){
              dp[i]=Math.max(nums[start+i]+dp[i-2],dp[i-1]);
            }
            return dp[size-1];
            

     }
    
}