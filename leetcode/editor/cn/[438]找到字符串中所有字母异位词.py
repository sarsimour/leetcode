
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left, right = 0, 0
        des_len = len(p)
        res = []
        des_dict = {}
        for c_ in p:
            des_dict[c_] = des_dict.get(c_, 0) + 1
        window_count = {}
        while right < len(s):
            while right - left < des_len and right < len(s):
                new_char = s[right]
                window_count[new_char] = window_count.get(new_char, 0) + 1
                right += 1
            if all([window_count.get(char_, 0) == des_dict[char_] for char_ in des_dict.keys()]):
                res.append(left)
            this_char = s[left]
            window_count[this_char] -= 1
            left += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
