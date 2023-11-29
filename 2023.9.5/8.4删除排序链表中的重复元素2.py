# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
# 难度：medium
# 复杂度：时间复杂度O(n)，空间复杂度O(1)

# 解法:一次遍历
# 思路:注意这次我们需要使用一个哑节点(dummy node)指向链表的头节点,防止从head开始就是重复元素
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        # 当下一个元素存在并且下下个元素存在时在循环里进行删除重复元素操作
        while cur.next and cur.next.next:
            # 下一个元素和下下个元素相等
            if cur.next.val == cur.next.next.val:
                tmp = cur.next.val
                while cur.next and cur.next.val == tmp:  # 跳过重复元素
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
