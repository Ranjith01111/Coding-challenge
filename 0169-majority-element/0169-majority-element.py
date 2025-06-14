class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        final_result = None
        count = 0

        for i in nums:
            if count == 0:
                final_result = i
            if final_result == i:
                count += 1
            else:
                count -= 1
        return final_result