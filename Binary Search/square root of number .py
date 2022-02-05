#https://leetcode.com/problems/sqrtx/

def sqrt(num):
    start=0
    end=num
    while start<end:
        mid=(start+end)//2
        root = mid
        if mid*mid==num:
            
            return mid 
        elif mid*mid>num:
            end=mid-1
        else:
            start=mid+1
            root=mid
    return root

print(sqrt(120))