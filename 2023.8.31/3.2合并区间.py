# https://leetcode.cn/problems/merge-intervals/
# 难度：medium

# 解法：排序法
# 思路：将区间数组根据左边界排序之后，遍历区间数组，根据右边界是否小于上一个区间的右边界判断是否需要合并
# 复杂度：时间复杂度O(nlogn),空间复杂度O(logn)


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 根据区间左边界排序
        intervals.sort(key=lambda x: x[0])
        # merged数组存储结果
        merged = []
        # 遍历区间数组
        for interval in intervals:
            # 列表为空或者当前区间与上一区间不重合
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则与上一区间合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
