# https://leetcode.cn/problems/majority-element/description/
# 难度：simple

import collections
from typing import List


# 解法一：哈希表
# 思路:将元素和出现次数存储在哈希表里,元素为键,出现次数为值
# 复杂度:时间复杂度O(n),空间复杂度O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Python中的一个内置函数，它用于统计可迭代对象中各个元素的出现次数，并以字典的形式返回统计结果
        counts = collections.Counter(nums)
        # 第一个参数是参与展示的列表（返回键），第二个参数是比较的列表（参与比较的值）
        return max(counts.keys(), key=counts.get)


# 解法二:排序
# 思路：排序之后索引n/2取下界的值必定为众数，因为题目中说众数的出现次数大于n/2的下界
# 复杂度：时间复杂度O(nlogn)，空间复杂度O(logn)，因为使用了语言自带的方法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
