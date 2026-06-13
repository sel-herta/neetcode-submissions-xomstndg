# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = ""
        def dfs(node):
            nonlocal serialized
            if not node:
                serialized += "N,"
                return
            serialized += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        print(serialized)
        return serialized
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nums = []
        currNum = ""
        for i in range(len(data)):
            if data[i] == ",":
                nums.append(currNum)
                currNum = ""
            else:
                currNum += data[i]
        print(nums)
        currI = 0
        def dfs():
            nonlocal currI
            if nums[currI] == "N":
                currI += 1
                return
            rootVal = int(nums[currI])
            root = TreeNode(rootVal)
            currI += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
            