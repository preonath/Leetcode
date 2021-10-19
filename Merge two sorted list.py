def mergeTwoLists(l1, l2):
        if not (l1 and l2):
            return l1 or l2
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next =mergeTwoLists(l1.next, l2)
        return l1
l1=input()
l2=input()
mergeTwoLists(l1,l2)