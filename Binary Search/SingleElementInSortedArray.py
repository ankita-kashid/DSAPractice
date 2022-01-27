""" 
1. For checking single element in sorted array by using binary search we can check whether the mid element is 
greater than the previous element and less than the next element
2. If mid is equal to mid+1, then we can increment in the mid
3. After that we will check the length from start to mid is even or odd, if it is odd then we will shift high to mid-2
and if it is even then we will increment start pointer

"""
def single(nums):
    start=0
    end=len(nums)-1
    while start<end:
        mid=(start+end)//2
        if start<mid<end and nums[mid-1]<nums[mid]<nums[mid+1]:
            return nums[mid]
        elif mid<end and nums[mid]==nums[mid+1]:
            mid+=1
        if (mid-start+1)%2!=0:
            end=mid-2
        else:
            start=mid+1
    return nums[start]
print(single([1,1,2,3,3,4,4,8,8]))
