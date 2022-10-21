
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) -1
        while True:
            if left >= right:
                raise ValueError
            if numbers[left] == target - numbers[right]:
                return [left + 1, right + 1]
            elif numbers[left] > target - numbers[right]:
                right = right -1
            else:
                left = left +1

# leetcode submit region end(Prohibit modification and deletion)
