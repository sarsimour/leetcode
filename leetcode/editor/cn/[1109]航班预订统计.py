
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        import numpy as np
        dif_array = np.zeros(n + 1, dtype=int)
        for begin_, end_, num_ in bookings:
            dif_array[begin_ - 1] += num_
            dif_array[end_] -= num_
        sum_array = np.cumsum(dif_array)
        return list(sum_array[:n])
# leetcode submit region end(Prohibit modification and deletion)
