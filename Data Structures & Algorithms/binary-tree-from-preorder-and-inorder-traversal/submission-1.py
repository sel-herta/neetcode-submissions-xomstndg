# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first element in preorder is the root of the tree
        # the first "return" from DFS is the first element in the inorder list
        inorderMapping = {}
        for i, val in enumerate(inorder):
            inorderMapping[val] = i
        
        self.currIndexPreorder = 0
        def dfs(l, r):
            if l > r:
                return
            rootVal = preorder[self.currIndexPreorder]
            self.currIndexPreorder += 1
            newNode = TreeNode(rootVal, None, None)
            inorderIndex = inorderMapping[rootVal]
            newNode.left = dfs(l, inorderIndex - 1)
            newNode.right = dfs(inorderIndex + 1, r)
            return newNode
        return dfs(0, len(inorder) - 1)

            

