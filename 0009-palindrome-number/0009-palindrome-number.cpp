class Solution {
public:
    bool isPalindrome(int x) {
        int temp = x;
   long rev = 0;

        while(temp > 0){
            int d = temp % 10;
            rev = rev * 10 + d;

            temp /= 10;
        }

        if(rev == x){
            return true;
        }else{
            return false;
        }

         
    }
};