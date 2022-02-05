class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def rev(head):
    prev=None
    curr=head
    while curr:
        nextt=curr.next
        curr.next=prev
        prev=curr
        curr=nextt
    return prev

########################### Taking Input for linkedlist ##################################

def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end='')
        head=head.next
    print("None")
    return
def takeInput():
    inputList=[int (ele) for ele in input().split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
#################################################################################333




head=takeInput()
printLL(head)
a=rev(head)
printLL(a)