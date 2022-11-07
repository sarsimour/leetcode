
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        res = 0
        window_count = {}
        while right < len(s):
            new_char = s[right]
            window_count[new_char] = window_count.get(new_char, 0) + 1
            right += 1
            while window_count[new_char] > 1:
                this_char = s[left]
                window_count[this_char] -= 1
                left += 1
            res = max(res, right - left)
        return res
# leetcode submit region end(Prohibit modification and deletion)
