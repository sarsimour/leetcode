
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""
        t_count = {}
        for char_ in t:
            t_count[char_] = t_count.get(char_, 0) + 1
        s_count = {}
        left, right = 0, 0
        best_res = (0, len(s))
        has_res = False
        while right < len(s):
            right += 1
            s_count[s[right - 1]] = s_count.get(s[right - 1], 0) + 1
            # print(s_count, left, right)
            while all([s_count.get(char_, 0) >= t_count[char_] for char_ in t_count.keys()]):
                has_res = True
                s_count[s[left]] -= 1
                left += 1
            if has_res and right - left + 1 < best_res[1] - best_res[0]:
                best_res = (left - 1, right)

        return s[best_res[0]: best_res[1]] if has_res else ""
# leetcode submit region end(Prohibit modification and deletion)
