


"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.


"""
def search(nums,start,end):
    pass

def findmin(nums):
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)//2
        while start<end and nums[start]==nums[end]:
            start+=1
        if nums[start]<nums[end]:
            return nums[0]
        a=search(nums,start,end)
        return a

print(findmin([4,5,6,7,0,1,4]))