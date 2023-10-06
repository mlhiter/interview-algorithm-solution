# https://leetcode.cn/problems/find-peak-element/description/
# 难度：medium


from typing import List

# 解法一：二分查找
# 思路：我们只需要找到其中一个峰值即可，根据“人往高处走”一定能找到一个峰值
# 复杂度：时间复杂度O(logn),空间复杂度O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 注意由于边界也有可能是峰值（因为题目告知nums[-1] = nums[n] = -∞）
        # 但是我们通过下标无法获得-1和n处的值，所以设置一个辅助函数
        def get(i:int)->int:
            if i==-1 or i==len(nums):
                return float('-inf')
            return nums[i]

        left,right = 0,len(nums)-1
        while left<=right:
            mid = left +(right-left)//2
            # 终止条件
            if get(mid-1)<get(mid)>get(mid+1):
                return mid
            # 二分查找
            # 因为相邻项必定不相等，所以不需要考虑等于的情况
            if get(mid)<get(mid+1):#峰值在右侧
                left = mid+1
            else:
                right = mid-1
        # 因为必定有峰值，所以不需要做错误处理
