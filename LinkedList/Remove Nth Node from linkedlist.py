
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



def remove(head,n):
    if not head or not head.next:
        return None
        
    p=q=t=head
    flag=0
    count=0
    prev=None
    while t:
        if count==n:
            p=t
            flag=1
        if flag:
            prev=q
            q=q.next
        count+=1
        t=t.next
    if prev:
        prev.next=q.next
    else:
        return q.next
    printLL(head)
    return head


head=takeinput()

ans=remove(head,4)

printLL(ans)


