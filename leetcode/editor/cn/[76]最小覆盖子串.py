
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
        for char_ in s:
            s_count[char_] = s_count.get(char_, 0) + 1
        left, right = 0, len(s) - 1
        able_to_right, able_to_left = True, True
        while left < right:
            if not able_to_left and not able_to_right:
                if any([s_count.get(char_, 0) < t_count[char_] for char_ in t_count.keys()]):
                    return ""
                else:
                    return s[left: right + 1]
            if able_to_right and (s[left] not in t_count.keys() or s_count.get(s[left], 0) > t_count[s[left]]):
                s_count[s[left]] -= 1
                left = left + 1
                if s[left] in t_count.keys() and s_count[s[left]] == t_count[s[left]]:
                    able_to_right = False
            if able_to_left and (s[right] not in t_count.keys() or s_count.get(s[right], 0) > t_count[s[right]]):
                s_count[s[right]] -= 1
                right -= 1
                if s[right] in t_count.keys() and s_count[s[right]] == t_count[s[right]]:
                    able_to_left = False

        return ""
# leetcode submit region end(Prohibit modification and deletion)
