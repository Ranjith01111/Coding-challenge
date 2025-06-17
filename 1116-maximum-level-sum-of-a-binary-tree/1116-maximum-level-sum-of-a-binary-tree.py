# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        max_sum = root.val
        max_level = 1

        queue = [root]
        cur_level = 1

        while queue:
            cur_level_total = len(queue)
            cur_level_sum = 0

            for i in range(cur_level_total):
                cur_node = queue.pop(0)
                cur_level_sum += cur_node.val
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)
            if cur_level_sum > max_sum:
                max_sum = cur_level_sum
                max_level = cur_level
            cur_level += 1
        return max_level