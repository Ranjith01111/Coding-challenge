class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:

            temp_result = []
            for subset in result:
                new_subset = subset + [i]
                temp_result.append(new_subset)
            result += temp_result
        return result