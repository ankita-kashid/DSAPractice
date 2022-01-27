"""
Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10
"""


def closest(nums,x):
    l=0
    r=len(nums)-1
    diff= 100000
    while l < r:
        if abs(nums[l]+nums[r]-x)<diff:
            a=l 
            b=r
            diff=abs(nums[l]+nums[r]-x)
        if nums[l]+nums[r]==x:
            return x
        if nums[l]+nums[r]<x:
            l+=1
        else:
            r-=1
    return [nums[a],nums[b]]


print(closest([10, 22, 28, 29, 30, 40],54))