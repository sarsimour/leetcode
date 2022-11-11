
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False
        des = {}
        for char_ in s1:
            des[char_] = des.get(char_, 0) + 1
        temp = {}
        for char_ in s2[: len1]:
            temp[char_] = temp.get(char_, 0) + 1
        for ind in range(len2 - len1 + 1):
            # print(des, temp)
            if all(temp.get(char_, 0) == des[char_] for char_ in des.keys()):
                return True
            if ind + len1 == len2:
                return False
            temp[s2[ind]] -= 1
            temp[s2[ind + len1]] = temp.get(s2[ind + len1], 0) + 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
