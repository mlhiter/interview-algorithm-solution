# https://leetcode.cn/problems/search-in-rotated-sorted-array/description/
# 难度：medium


# 三种解法
# 解法一：将旋转数组查找目标值转换为有序数组查找目标值
# 思路：先完成[寻找旋转排序数组中的最小值]，将旋转数组转换为两段有序数组，然后比较nums[0]与target判断target在哪一段，然后再使用二分查找在那一段进行查找。
# 复杂度：时间复杂度O(logn),空间复杂度O(1)
import sys
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1,先找到最小值
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        minIndex = right

        # 重置边界值
        left, right = 0, len(nums) - 1

        # 2,判断target在左边段还是右边段
        if (
            target >= nums[0] and nums[0] > nums[minIndex]
        ):  # target在左半段，这里如果没有and后半部分的话，如果原数组本来就是有序递增数组时是不对的
            # 3,进行该段内的二分查找
            right = minIndex  # 当只有一个元素的时候会出错(如果-1的话)
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # 没找到就返回-1
            return -1
        else:
            # 3,进行该段内的二分查找
            left = minIndex
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1


# 解法二：解法一的衍生解法
# 思路：先比较nums[0]和target的大小，判断target在哪一段，然后将另一段变成极值（逐渐满足有序数组的要求，左段要改变就赋值为-inf，右段要改变就赋值为inf）。
# 复杂度：时间复杂度O(logn),空间复杂度O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # 1,先判断target在左半段还是右半段,将另一半段置为最大值或最小值
            if target >= nums[0]:
                if nums[mid] < nums[0]:  # 右半段
                    nums[mid] = sys.maxsize  # 最大的int
            else:
                if nums[mid] >= nums[0]:  # 左半段
                    nums[mid] = -sys.maxsize - 1
            # 2,进行正常的二分缩小范围
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# 解法三：比较绕的方法，将解法一的过程组合一下
# TODO：暂不实现，之后待实现
# 先根据 nums[mid] 与 nums[left] 的关系判断 mid 是在左段还是右段，接下来再判断 target 是在 mid 的左边还是右边，从而来调整左右边界 left 和 right
