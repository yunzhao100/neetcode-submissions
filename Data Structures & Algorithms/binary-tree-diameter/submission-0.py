# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0

        # return height, update self.res
        def dfs(curr):
            if not curr: return 0
            height_left=dfs(curr.left)
            height_right=dfs(curr.right)
            # diameter of a node is the left height plus the right height
            self.res=max(self.res,height_left+height_right)
            return max(height_left,height_right)+1

        dfs(root)
        return self.res