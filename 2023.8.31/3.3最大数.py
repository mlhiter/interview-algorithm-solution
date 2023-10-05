# https://leetcode.cn/problems/largest-number/description/
# 难度：medium


# 解法：贪心
# 思路：https://leetcode.cn/problems/largest-number/solutions/1/179-zui-da-shu-tan-xin-qing-xi-tu-jie-by-wboz/
# 复杂度：时间复杂度O(nlogn),空间复杂度O(logn)
import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 将数字数组nums通过str函数转换为字符串数组strs
        strs = map(str, nums)

        # 自定义排序函数
        # 比较一下两个字符串拼接之后的数的值大小即可，按照从大到小排列就是最大数
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1

        # 对字符串进行排序
        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        # 如果字符串首字母为0则返回0
        return "".join(strs) if strs[0] != "0" else "0"
