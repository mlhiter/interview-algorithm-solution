# https://leetcode.cn/problems/move-zeroes/
# 难度：simple

# 解法一：冒泡排序
# 思路：通过冒泡排序将零不断后移到最后位置，由于排序稳定性所以不会改变原有的顺序，但是这种方法会超时


from typing import List


# 解法二:两次遍历法
# 思路:第一次遍历将所有非零元素前移,第二次将倒数零的个数的元素赋值为0即可
# 复杂度：时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return 0
        # 第一次遍历
        # j记录非零元素个数
        j = 0
        for i in range(0, len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
