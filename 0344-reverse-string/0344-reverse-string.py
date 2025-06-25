class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for i in s:
            stack.append(i)
        i = 0 
        while len(stack) > 0:
            m = stack.pop()
            s[i] = m
            i+=1 