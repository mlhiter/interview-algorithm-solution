# https://leetcode.cn/problems/single-number/description/
# 难度：simple

# 解法：位运算
# 思路：异或操作满足我们的题目要求
# 异或操作：一个数和0异或后不变，任何数和自身异或为0，异或操作满足交换律和结合律
# 复杂度：时间复杂度O(n),空间复杂度O(1)
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
