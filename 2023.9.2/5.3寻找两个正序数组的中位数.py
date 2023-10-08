# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
# 难度：hard


from typing import List


# 题目要求:时间复杂度为O(log(m+n)),一眼二分查找
# 解法:二分查找
# 复杂度：时间复杂度O(log(m+n))，空间复杂度O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 函数：寻找两个数组第k小元素（二分查找）
        def getKthElement(k):
            startIndex1, startIndex2 = 0, 0  # 用来记录两个数组左边界索引

            # 二分查找排除过程（不断更新左边界）
            while True:
                # 特殊情况（终止条件）
                if startIndex1 == m:  # 第一个数组全部元素被排除
                    return nums2[startIndex2 + k - 1]
                if startIndex2 == n:  # 第二个数组全部元素被排除
                    return nums1[startIndex1 + k - 1]
                if k == 1:  # 返回两剩余数组元素的最小值即可
                    return min(nums1[startIndex1], nums2[startIndex2])

                # 正常情况

                # 这两行作用：如果startIndex+(k//2-1)越界（超过数组最大索引了），我们需要选取该数组最后一个元素
                newStartIndex1 = min(startIndex1 + k // 2 - 1, m - 1)
                newStartIndex2 = min(startIndex2 + k // 2 - 1, n - 1)

                # 标志数，用来判断更新哪个数组
                pivot1, pivot2 = nums1[newStartIndex1], nums2[newStartIndex2]
                if pivot1 <= pivot2:
                    # TODO:这里的更新过程有点懵，看了好一会没看明白，这里需要再解决一下
                    k -= (newStartIndex1 + 1) - startIndex1  # 更新k值,减去排除的数字的个数
                    startIndex1 = newStartIndex1 + 1  # 更新startIndex值
                else:
                    k -= (newStartIndex2 + 1) - startIndex2
                    startIndex2 = newStartIndex2 + 1

        # 主程序
        m, n = len(nums1), len(nums2)
        totalLength = m + n

        if totalLength % 2 == 1:  # 奇数组
            return getKthElement((totalLength + 1) // 2)
        else:  # 偶数组
            return (
                getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)
            ) / 2
