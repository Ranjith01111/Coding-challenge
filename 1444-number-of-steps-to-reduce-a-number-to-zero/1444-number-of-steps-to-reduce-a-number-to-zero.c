
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


int numberOfSteps(int num) {
      return ranjith(num,0);
}
