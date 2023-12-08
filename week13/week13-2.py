class Solution:
    #要使用之前教過的'函式呼叫函式'
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root == None:return""

        now=str(root.val)
        left=self.tree2str(root.left)
        right=self.tree2str(root.right)

        if left==""and right=="":return now
        if right=="":return now+"("+left+")"
        return now+"("+left+")("+right+")"