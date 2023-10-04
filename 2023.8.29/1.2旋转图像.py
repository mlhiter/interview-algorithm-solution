# https://leetcode.cn/problems/rotate-image/
# 难度：medium

# 解法一：翻转代替旋转
# 思路：先水平翻转再主对角线翻转
# 复杂度：时间复杂度O(n^2) 空间复杂度O(1)
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
