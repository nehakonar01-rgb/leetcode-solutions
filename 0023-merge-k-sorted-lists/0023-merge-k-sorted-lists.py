import heapq

class Solution:
    def mergeKLists(self, lists):

        dummy = ListNode(0)
        current = dummy

        heap = []

        # Put first node of every list into heap
        for i in range(len(lists)):

            if lists[i]:
                heapq.heappush(
                    heap,
                    (lists[i].val, i, lists[i])
                )

        # Process heap
        while heap:

            value, index, node = heapq.heappop(heap)

            # Add smallest node to result
            current.next = node
            current = current.next

            # Add next node from same list
            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, index, node.next)
                )

        return dummy.next