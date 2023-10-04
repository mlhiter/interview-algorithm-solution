# https://leetcode.cn/problems/sort-an-array/description/
# 难度：medium

from typing import List


# 解法一：归并排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1, temp)
        return nums

    # 归并排序
    def mergeSort(self, nums, left, right, temp):
        # 优化一：小区间使用插入排序
        if right - left < 16:
            self.insertionSort(nums, left, right)
            return
        mid = (left + right) // 2
        # 这里不考虑整型溢出的情况
        self.mergeSort(nums, left, mid, temp)
        self.mergeSort(nums, mid + 1, right, temp)
        # 优化二：如果数组已经有序则不需要合并操作
        if nums[mid] <= nums[mid + 1]:
            return

        # 合并有序区间
        # 赋值给辅助数组
        for i in range(left, right + 1):
            temp[i] = nums[i]
        i, j = left, mid + 1
        for k in range(left, right + 1):
            if i == mid + 1:
                nums[k] = temp[j]
                j = j + 1
            elif j == right + 1:
                nums[k] = temp[i]
                i = i + 1
            elif temp[i] <= temp[j]:
                nums[k] = temp[i]
                i = i + 1
            else:
                nums[k] = temp[j]
                j = j + 1

    # 插入排序
    def insertionSort(self, nums, left, right):
        for i in range(left + 1, right + 1):
            temp = nums[i]
            j = 0
            for j in range(i, left - 1, -1):
                if nums[j - 1] > temp:
                    nums[j] = nums[j - 1]
                else:
                    break
            nums[j] = temp
