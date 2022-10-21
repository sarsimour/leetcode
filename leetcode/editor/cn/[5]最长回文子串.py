
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_s = ''
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)
            max_s = s1 if len(max_s) < len(s1) else max_s
            max_s = s2 if len(max_s) < len(s2) else max_s
        return max_s

    def palindrome(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left + 1: right]

# leetcode submit region end(Prohibit modification and deletion)
