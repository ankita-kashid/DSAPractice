
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 

def detectCycle(head):
    print(head)
 
    
 
 
if __name__ == '__main__':
 
    head = None
    for i in reversed(range(5)):
        head = Node(i + 1, head)
 
    # insert cycle
    head.next.next.next.next.next = head.next.next
 
    if detectCycle(head):
        print('Cycle Found')
    else:
        print('No Cycle Found')