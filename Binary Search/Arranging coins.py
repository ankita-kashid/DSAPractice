#https://leetcode.com/problems/arranging-coins/

def coins(num):
    start=0
    end=num
    while start<=end:
        mid=(start+end)//2
        if (mid*(mid+1))//2 <=num:
            start=mid+1
        else:
            end=mid-1
    return start-1

print(coins(5))