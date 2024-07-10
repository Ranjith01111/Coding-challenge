class Solution(object):
    def twoSum(self, nums, target):

        numin = {}
        for i, num in enumerate(nums):
            com = target - num
            if com in numin:
                return [numin[com], i]
            numin[num] = i
        return []
    
        