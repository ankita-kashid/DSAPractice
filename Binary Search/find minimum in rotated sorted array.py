"""
[3,4,5,1,2]
[4,5,6,7,0,1,2]
[11,13,15,17]
[1,2]
[2]
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

def minimum(nums):
    start=0
    end=len(nums)-1
    while start<end:
        mid=(start+end)//2
        if nums[mid-1]>nums[mid] and nums[mid+1]>nums[mid]:
            return nums[mid]
        elif nums[start]>nums[end] and nums[mid]>nums[end]:
            start=mid+1
        else:
            end=mid-1


print(minimum([4,5,6,7,0,1,2]))