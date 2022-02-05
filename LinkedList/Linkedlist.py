
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    while head is not None:
        print(str(head.data)+"-->",end="")
        head=head.next
    print("None")
    #return


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




head=takeinput()
printLL(head)
