class Solution(object):
    def removeElement(self, nums, val):
        s = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[s] = nums[i]
                s+=1
        return s
        