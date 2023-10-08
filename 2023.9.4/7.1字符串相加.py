# https://leetcode.cn/problems/add-strings/description/
# 难度：simple


# 解法：双指针法
# 思路：两个指针模拟数字相加的过程，从最后一位开始相加，注意进位处理以及两个数字不一样位时的处理即可
# 复杂度：时间复杂度O(max(m,n)),空间复杂度O(max(m,n));m,n为两个数字字符串的长度
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        # 两个指针i,j以及代表进位数的carry
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            # 如果该位没有数，则用0
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry  # 当前数 = 对应位数相加加上进位数
            carry = tmp // 10  # 是否进位
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        # 如果最前一位进位则在最前面加上1
        return "1" + res if carry else res
