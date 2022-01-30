#https://leetcode.com/problems/valid-perfect-square/

def isperfect(num):
    start=0
    end=num
    while start<=end:
        mid=(start+end)//2
        if mid*mid==num:
            return mid
        elif mid*mid>num:
            end=mid-1
        else:
            start=mid+1
    return 0


print(isperfect(25))