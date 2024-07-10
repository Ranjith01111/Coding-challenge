class Solution(object):
    def balancedStringSplit(self, s):
        list=[0,0]
        count=0
        for letter in s:
            if letter == "L":
                list[0]+=1
            else:
                list[1]+=1
            if(list[0]==list[1]):
                count+=1
                list[0]=0
                list[1]=0
        return(count)            
