# https://leetcode.cn/problems/sliding-window-maximum/description/
# 难度：hard

# 解法一：优先队列
# 思路：考虑到相邻的窗口之间公用较多元素，可以使用大根堆实时维护一系列元素中的最大值。
# 复杂度:时间复杂度O(nlogn),空间复杂度O(k)
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # python中默认的优先队列是小根堆，它的q[0]为堆内最小值，所以这里需要转换一下
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:  # 当最大值不在窗口内时就从堆内删除该最大值，保证最大值在窗口内部
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans


# TODO:这个题还有很多更高级的解法，这里留着之后添加
