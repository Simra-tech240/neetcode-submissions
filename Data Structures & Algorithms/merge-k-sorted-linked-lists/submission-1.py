class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        def merge_two_lists(a, b):
            dummy = ListNode(0)
            current = dummy

            while a and b:
                if a.val <= b.val:
                    current.next = a
                    a = a.next
                else:
                    current.next = b
                    b = b.next

                current = current.next

            current.next = a if a else b
            return dummy.next

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge_two_lists(first, second))

            lists = merged

        return lists[0] if lists else None