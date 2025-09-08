class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tot = (n*(n+1))//2
        actual_value = sum(nums)
        return tot - actual_value