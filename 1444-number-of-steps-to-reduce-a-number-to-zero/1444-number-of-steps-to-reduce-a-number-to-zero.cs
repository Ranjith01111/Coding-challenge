public class Solution {
    public int NumberOfSteps(int num) {
         return ranjith(num,0);

}
int ranjith(int num , int steps){
        if(num == 0){
            return steps; 
        }

        if(num %2 ==0){
            return ranjith(num/2,steps+1);
        }else{
            return ranjith(num-1,steps+1);
        }

}
}