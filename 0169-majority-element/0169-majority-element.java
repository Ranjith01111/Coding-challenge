class Solution {
    public int majorityElement(int[] nums) {
        int final_input = 0;
        int count = 0;

        for(int i=0;i<nums.length;i++){
            if(count == 0){
                final_input = nums[i];
            }
            if (final_input == nums[i]){
                count += 1;
            }
            else{
                count -= 1;
            }
        }
        return final_input;
    }
}