class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            total = num1 + num2 + carry
            carry = total // 10
            total %= 10

            result.next = ListNode(total)
            result = result.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result_tail.next
