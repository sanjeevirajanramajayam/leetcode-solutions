class Solution {
    public boolean sub(int[] nums,int start,int end){
        Set<Integer> seen = new HashSet<>();
        int ecount=0;
        int ocount=0;
        for(int i=start;i<=end;i++){
            if(seen.contains(nums[i])){
                continue;
            }
            seen.add(nums[i]);
            if(nums[i]%2==0){
                ecount++;
            }
            else{
                ocount++;
            }
        }
        return ecount == ocount;
    }
    public int longestBalanced(int[] nums) {
        int n = nums.length;
        int maxLen = 0;
        for(int i =0;i<n;i++){
            Set<Integer> seen = new HashSet<>();
            int ecount=0;
            int ocount=0;
            for(int j=i;j<n;j++){
                if(seen.add(nums[j])){
                    if(nums[j]%2==0){
                        ecount++;
                    }
                    else{
                        ocount++;
                    }
                }
                if(ecount == ocount){
                    maxLen = Math.max(maxLen,j-i+1);
                }
            }
        }
        return maxLen;
    }
}