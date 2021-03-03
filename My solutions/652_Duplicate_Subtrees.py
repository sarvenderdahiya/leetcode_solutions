# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        dup = []
        count_subt = collections.Counter()
        
        def dfstree(node):
            if not node:
                return ''
            subtree = f"{node.val},{dfstree(node.left)},{dfstree(node.right)}" 
            #print (type(subtree))
            count_subt[subtree] +=1
            if count_subt[subtree] == 2:
                dup.append(node)
            return subtree
        
        dfstree(root)
        return dup