# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
#  有效 二叉搜索树定义如下：
#
#
#  节点的左子树只包含 小于 当前节点的数。
#  节点的右子树只包含 大于 当前节点的数。
#  所有左子树和右子树自身必须也是二叉搜索树。
#
#
#
#
#  示例 1：
#
#
# 输入：root = [2,1,3]
# 输出：true
#
#
#  示例 2：
#
#
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#
#
#
#
#  提示：
#
#
#  树中节点数目范围在[1, 10⁴] 内
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 2215 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _sub(root):
            if root is None:
                return (True, None, None)
            else:
                left_res = _sub(root.left)
                right_res = _sub(root.right)
                if not left_res[0] or not right_res[0]:
                    res = (False, None, None)
                else:
                    if left_res[2] is not None and left_res[2] >= root.val:
                        res = (False, None, None)
                    elif right_res[1] is not None and right_res[1] <= root.val:
                        res =  (False, None, None)
                    else:
                        left_val = left_res[1] if left_res[1] is not None else root.val
                        right_val = right_res[2] if right_res[2] is not None else root.val
                        res = (True, left_val, right_val)
                return res

        if root is None:
            return True
        res = _sub(root)
        return res[0]


# leetcode submit region end(Prohibit modification and deletion)
