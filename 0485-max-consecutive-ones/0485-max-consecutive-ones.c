int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int maxcount = 0;
    int count = 0;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] == 1){
            count += 1;
            if(maxcount < count){
                maxcount = count;
            }
        }
        else{
            count = 0;    
        }
    }
    return maxcount;
}
