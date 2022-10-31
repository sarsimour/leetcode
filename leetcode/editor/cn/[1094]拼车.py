
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        import numpy as np
        dif_array = np.zeros(1001)
        max_to = 0
        for num_, begin_, end_ in trips:
            dif_array[begin_] += num_
            dif_array[end_] -= num_
            max_to = max(max_to, end_)

        max_num = 0
        for ind in range(max_to + 1):
            max_num += dif_array[ind]
            if max_num > capacity:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
