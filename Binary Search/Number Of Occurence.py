"""
nums=[1, 1, 1,2, 2, 2, 2, 3]
x=2
"""
def occurence(nums,x):
    n=len(nums)
    if n==1 and x!=n:
        return 0
    if n==1 and x==n:
        return 1
    start=0
    c=0
    end=len(nums)-1
    while start<=end:
        
        mid=(start+end)//2
        print(mid,start,end)
        if  nums[mid]==x and nums[mid-1]!=x:
            while mid<=len(nums)-2 and nums[mid]==nums[mid+1]:
                mid+=1
                c+=1
            return c+1
        elif  nums[mid]<x:
            print("elif")
            start=mid+1
        else:
            print("else")
            end=mid-1
    return 0
print(occurence([8,8],8))
