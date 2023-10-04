# https://leetcode.cn/problems/kth-largest-element-in-an-array/
# 难度：medium
# 知识点：堆、快速排序

# 解法一：暴力解法
# 思路：直接调用标准函数
# 复杂度：时间复杂度O(NlogN) 空间复杂度O(logN)
from random import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        nums.sort()
        return nums[size - k]


# TODO:快速排序和堆排序都还没理解和实现
# 解法二：快速排序
# 思路：
# 复杂度:
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(left, right, k):
            # 随机化
            rand_idx = random.randint(left, right)
            nums[rand_idx], nums[left] = nums[left], nums[rand_idx]

            i, j = left, right
            while i < j:
                while nums[j] >= nums[left] and i < j:
                    j -= 1
                while nums[i] <= nums[left] and i < j:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[left] = nums[left], nums[i]
            if i == right + 1 - k:
                return nums[i]
            elif i < right + 1 - k:
                return quickSelect(i + 1, right, k)
            else:
                return quickSelect(left, i - 1, k - (right - i + 1))

        n = len(nums)
        left, right = 0, n - 1
        return quickSelect(left, right, k)
