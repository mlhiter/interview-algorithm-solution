# https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description/
# 难度：medium

# 解法一：动态规划
# TODO:动态规划解法先不写，留待以后


# 解法二：滑动窗口
# 思路：暴力求解时间复杂度高的原因是相同位置比较多次,我们可以通过固定起始位置然后比较上下对应位置的值相邻相同数量即可
# 复杂度:时间复杂度O((N+M)*min(N,M))，空间复杂度O(1)
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 找当前对齐方式下窗口内两数组一一对应部分子数组的长度
        # addA和addB分别为窗口在A和B的起始索引，length为窗口长度
        def maxLength(addA: int, addB: int, length: int) -> int:
            ans = k = 0
            for i in range(length):
                if nums1[addA + i] == nums2[addB + i]:
                    k += 1
                    ans = max(ans, k)
                else:  # 两者不相同直接赋值为0
                    k = 0
            return ans

        # 主程序
        n, m = len(nums1), len(nums2)
        ret = 0

        # 枚举A和B所有的对齐方式
        # A不变,B的首元素与A中的某个元素对齐
        for i in range(n):
            length = min(m, n - i)  # 每次迭代选用数组B的长度和剩余长度的较小值作为长度,是考虑到数组B可能短于数组A
            ret = max(ret, maxLength(i, 0, length))
        # B不变,A的首元素与B中的某个元素对齐
        for i in range(m):
            length = min(n, m - i)
            ret = max(ret, maxLength(0, i, length))
        return ret
