
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        dim = len(matrix)
        for i in range(dim):
            for j in range(i, dim):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(dim):
            for j in range(int(dim / 2)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][dim - j - 1]
                matrix[i][dim - j - 1] = temp

# leetcode submit region end(Prohibit modification and deletion)
