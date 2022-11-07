
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        upper_bound = 0
        lower_bound = len(matrix) - 1
        left_bound = 0
        right_bound = len(matrix[0]) - 1
        side = 'r'
        times = 0
        res = []
        while True:
            if times % 4 == 0:
                res += matrix[upper_bound][left_bound: right_bound + 1]
                upper_bound += 1
            elif times % 4 == 1:
                res += [matrix[row_][right_bound] for row_ in range(upper_bound, lower_bound + 1)]
                right_bound -= 1
            elif times % 4 == 2:
                res += matrix[lower_bound][left_bound: right_bound + 1][::-1]
                lower_bound -= 1
            elif times % 4 == 3:
                res += [matrix[row_][left_bound] for row_ in range(upper_bound, lower_bound + 1)][::-1]
                left_bound += 1

            # print(res)
            # print(upper_bound, lower_bound, left_bound, right_bound, times)
            if times % 4 in (0, 2) and right_bound < left_bound:
                break
            if times % 4 in (1, 3) and lower_bound < upper_bound:
                break
            times += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
