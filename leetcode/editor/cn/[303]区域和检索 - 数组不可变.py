
# leetcode submit region begin(Prohibit modification and deletion)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum_pre = [0]
        self._get_sum_pre()

    def _get_sum_pre(self):
        for ind, value in enumerate(self.nums):
            self.sum_pre.append(value + self.sum_pre[-1])


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return int(self.sum_pre[right+1] - self.sum_pre[left])





# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
