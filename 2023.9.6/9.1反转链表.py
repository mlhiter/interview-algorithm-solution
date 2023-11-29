# https://leetcode.cn/problems/reverse-linked-list/description/
# 难度：simple

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 解法一:迭代
# 思路: 两个指针即可完成任务，prevNode指向前一个节点，cur指向当前节点
# 复杂度:时间复杂度O(n),空间复杂度O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prevNode = None

        cur = head

        while cur:
            nextNode = cur.next  # 当前节点下一个节点暂存到nextNode内
            cur.next = prevNode  # 将当前节点的下一个节点指向prevNode(原来链表的当前节点的上一个节点)
            prevNode = cur  # 将当前节点暂存到prevNode中
            cur = nextNode  # 将cur指向原链表的"当前节点的下一个节点",向后迭代
        return prevNode  # 迭代完成后prevNode指向原来链表最后一个节点


# 解法二：递归
# 思路：
# 复杂度：时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 终止条件
        if head == None or head.next == None:
            return head

        # 会将最后一个节点作为newHead一层层传递回来,你可以看到之后的逻辑不会涉及到newHead
        newHead = self.reverseList(head.next)

        # 改变节点之间的指向->反向
        head.next.next = head  # 这是最关键的一句(将原来链表中当前节点的下一个节点指向的下下个节点的指针指向当前节点,也就是反向)
        head.next = None  # 防止成环,这一步的作用在最后一个迭代有用,就是将新的链表的最后一个节点的下一个节点指向None
        return newHead
