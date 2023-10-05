# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
# 难度：medium

# 解法：二分查找
# 思路：做两次二分查找即可，分别找到元素的这两个位置
# 复杂度：时间复杂度O(logn)，空间复杂度O(1)

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        n = len(nums)
        # 数组长度为0时直接返回
        if n==0:
            return ans
        
        # 找元素的起始位置
        left,right = 0,n-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                ans[0] = mid
                right = mid-1 # 如果我们找到的是元素的非起始位置,则通过这里可以再往前找,目的是找起始位置
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        
        # 找元素的终止位置
        left,right = 0,n-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                ans[1] = mid
                left = mid+1 # 如果我们找到的是元素的非终止位置,则通过这里可以再往后找,目的是找终止位置
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return ans