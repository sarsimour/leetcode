# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
# 
#  Related Topics 字符串 动态规划 回溯 👍 3432 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        memos = {1: ["()"], 0: [""]}

        def _sub(n):
            if n == 1:
                return memos[1]
            else:
                if n in memos.keys():
                    return memos[n]
                memos[n] = []
                for p in range(n):
                    memos[n] += ["(" + item_l + ")" + item_r for item_l in _sub(p) for item_r in _sub(n-p-1)]
                return memos[n]

        return sorted(_sub(n))

# leetcode submit region end(Prohibit modification and deletion)
