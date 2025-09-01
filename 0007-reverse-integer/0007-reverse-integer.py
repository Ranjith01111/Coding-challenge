class Solution:
    def reverse(self, x: int) -> int:
        Min_val = -(2**31)
        Max_val = (2**31 - 1)

        sign = -1 if x < 0 else 1
        x = x*-1 if x < 0 else x
        rev = 0

        while(x):
            d = x%10
            rev = rev*10 + d
            x = x//10

        if(rev < Min_val or rev > Max_val):
            return 0
        
        return sign*rev