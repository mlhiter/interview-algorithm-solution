# https://leetcode.cn/problems/binary-search/
# 难度：simple


# 解法：二分查找
# 思路：因为数组已有序，通过nums[mid]和target的比较不断对半减少搜索空间，直到搜索到目标
# 复杂度：时间复杂度O(logn)，空间复杂度O(1)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            # 当nums[mid]为target直接返回
            if nums[mid] == target:
                return mid
            # 当target在mid右边时
            elif nums[mid] < target:
                left = mid + 1
            # 当target在mid左边时
            else:
                right = mid - 1
        # 没找到时直接返回-1
        return -1
