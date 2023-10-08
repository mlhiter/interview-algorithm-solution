# https://leetcode.cn/problems/sqrtx/description/
# 难度：simple


# 解法一:二分查找
# 思路:由于结果只需要整数,我们可以在[0,x]范围内二分查找,找到ans^2<=x的ans最大值即为结果
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
