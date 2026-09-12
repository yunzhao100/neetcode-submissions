# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue=deque()
        queue.append((root,float('-inf'),float('inf')))
        while queue:
            curr,left,right=queue.popleft()
            if not (left<curr.val<right):
                return False
            if curr.left:
                queue.append((curr.left,left,curr.val))
            if curr.right:
                queue.append((curr.right,curr.val,right))
        return True