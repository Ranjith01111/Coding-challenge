int subtractProductAndSum(int n) {
    int sum = 0,pro =1;
    while(n>0){
        int d= n%10;
        sum=sum + d;
        pro = pro*d;
        n=n/10;
    }
    int s = pro - sum;
    return s;   
}