int numWaterBottles(int numBottles, int numExchange) {
    int total = numBottles;
    int empty = numBottles;
    while(empty >= numExchange){
        int n = empty / numExchange;
        total = total+n;
        empty = empty % numExchange + n;
    }
    return total;
}