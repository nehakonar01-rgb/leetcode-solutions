class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            # Find the kth node
            kth = groupPrev

            for i in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            groupNext = kth.next

            # Reverse the current group
            prev = groupNext
            current = groupPrev.next

            while current != groupNext:

                nextNode = current.next

                current.next = prev

                prev = current
                current = nextNode

            # Save the old first node
            # It becomes the last node after reversal
            temp = groupPrev.next

            # Connect previous group to reversed group
            groupPrev.next = kth

            # Move groupPrev to the end of reversed group
            groupPrev = temp