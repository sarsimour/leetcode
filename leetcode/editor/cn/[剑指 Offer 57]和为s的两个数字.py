
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == target - nums[right]:
                return [nums[left], nums[right]]
            elif nums[left] > target - nums[right]:
                right -= 1
            else:
                left += 1
# leetcode submit region end(Prohibit modification and deletion)
