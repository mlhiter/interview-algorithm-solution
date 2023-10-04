# https://leetcode.cn/problems/merge-sorted-array/description/
# 难度：simple

# 解法一：双指针法
# 思路：从后向前遍历两个数组，将两者大的部分放到第一个数组的最后一个位置
# 时间复杂度：O（m+n）
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 放置位置指针
        k = m + n - 1
        # 两个数组的遍历指针
        i, j = m - 1, n - 1
        # 第二个数组还有元素未合并
        while j >= 0:
            # 第一个数组还有元素可以调整位置且符合条件时
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k = k - 1
