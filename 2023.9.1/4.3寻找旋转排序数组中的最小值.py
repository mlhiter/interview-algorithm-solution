# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/
# 难度:medium


# 解法:二分查找
# 思路:观察观察就能看出来,通过不断缩小搜索范围就可以找到最小值
# 复杂度：时间复杂度O(logn)，空间复杂度O(1)

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # 当区间元素数量大于1时继续循环,不断缩小范围
        while left < right:
            mid = left + (right - left) // 2
            # 中间值大于右端值,说明最小值在mid右侧
            if nums[mid] > nums[right]:
                left = mid + 1
            # 中间值大于等于右端值,说明最小值在mid左边或者就是mid
            else:
                right = mid
        return nums[right]
