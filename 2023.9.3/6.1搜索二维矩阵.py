# https://leetcode.cn/problems/search-a-2d-matrix-ii/description/
# 难度：medium
from typing import List


# 解法一：Z字形
# 思路：从右上角开始向左下角缩减范围，根据当前右上角值和target的比较忽略一行或者一列数据，直到找到该值
# 复杂度：时间复杂度O(m+n)，空间复杂度O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 从右上角开始遍历
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            # 如果当前值比target大，这一列都比target大，直接删除这一列
            if matrix[x][y] > target:
                y -= 1
            # 如果当前值比target小,这一行都比target小,直接删除这一行
            else:
                x += 1
        return False
    
# 解法二：暴力遍历搜索
# 复杂度：时间复杂度O(mn)，空间复杂度O(1)

# 解法三：简单二分查找
# 思路：遍历行，对每一行进行二分查找
# 复杂度：时间复杂度O(mlogn)，空间复杂度O(1)

# 解法四：优化二分查找
# 思路：遍历对角线元素，对该元素所在行该元素右侧元素进行二分查找，对该元素所在列下侧元素进行二分查找。
# 复杂度：时间复杂度O(min(m,n)*(logm+logn))
