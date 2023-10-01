def has_cycle(head):
    slow=fast=head
    while fast and fast.next:
        slow =slow.next
        fast=fast.next.next
        if fast==slow:return 1
    return  0
