# https://leetcode.cn/problems/spiral-matrix/
# 难度：medium

# 解法一：模拟
# 思路：定义四个方向，走到矩阵尽头或者遇到已经走过的元素就顺时针转向，当把所有的位置都走一遍之后模拟结束
# 复杂度：时间复杂度O(mn) 空间复杂度O(mn)
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 矩阵为空或者不是矩阵
        if not matrix or not matrix[0]:
            return list()

        # 定义矩阵初始属性
        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]  # 已经访问过的数据
        total = rows * columns
        order = [0] * total  # 结果数组

        # 初始化数据
        # 方向数据：右，下，左，上
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0

        # 开始循环模拟
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = (
                row + directions[directionIndex][0],
                column + directions[directionIndex][1],
            )
            # 如果下一个访问对象超过边界或者已经访问过
            if not (
                0 <= nextRow < rows
                and 0 <= nextColumn < columns
                and not visited[nextRow][nextColumn]
            ):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order


# 解法二：逐层模拟
# 思路：将矩阵分成每一层（圈），对每一圈进行顺时针模拟
# 复杂度：时间复杂度O(mn) 空间复杂度O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1

        while left <= right and top <= bottom:
            # 从左到右
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            # 从上到下
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            # 如果是多行多列
            if left < right and top < bottom:
                # 从右到左
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                # 从下到上
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order

# 解法三：代码量极致精简，然而很慢
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            # 削头（第一层）
            res += matrix.pop(0)
            # 将剩下的逆时针转九十度，等待下次被削
            matrix = list(zip(*matrix))[::-1]
        return res