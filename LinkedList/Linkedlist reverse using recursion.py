


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    while head is not None:
        print(str(head.data)+"-->",end="")
        head=head.next
    print("None")
    return


def takeinput():
    inputlist=[int(i) for i in input().split()]
    head=None
    tail=None
    for data in inputlist:
        if data==-1:
            break
        newNode=Node(data)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
def reverse1(head):
    if not head or not head.next:
        return head,head
    smallHead,smallTail=reverse1(head.next)
    smallTail.next=head
    head.next=None
    return smallHead,head


def reverse2(head):
    if not head or not head.next:
        return head
    smallHead = reverse2(head.next)
    tail=head.next
    tail.next=head
    head.next=None
    return smallHead

head=takeinput()
printLL(head)
#head,tail=reverse1(head)
#printLL(head)
head=reverse2(head)
printLL(head)