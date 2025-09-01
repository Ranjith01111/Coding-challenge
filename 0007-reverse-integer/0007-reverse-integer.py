class Solution:
    def reverse(self, x: int) -> int:
        Min_val = -2147483648
        Max_val = 2147483647

        sign = -1 if x < 0 else 1
        x = x*sign
        rev = int(str(x)[::-1])

        if(rev < Min_val or rev > Max_val):
            return 0
        
        return sign*rev