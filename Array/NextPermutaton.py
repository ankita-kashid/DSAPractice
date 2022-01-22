#nums=[1,2,3,4,5,3,5,4]
#out=[1,2,3,4,5,4,3,5]

# APPROACH
# We need to check untill the current element is less than the next element , if we find the greater element
# we will add this value to variable idx, will search from idx position to n  and check if current element is greater
#than idx-1 element and less than the prev element , once we get the element we will swap idx-1 and prev , and sort
#array from idx to n

def per(nums):
    idx=-1
    n=len(nums)
    for i in range(n-1,-1,-1):
        if nums[i-1]<nums[i]:
            idx=i
            break
    if idx==-1:
        return nums.sort()
    else:
        prev=idx
        for i in range(idx,n):
            if nums[i]>nums[idx-1] and nums[i]<nums[prev]:
                prev=i
        nums[idx-1],nums[prev]=nums[prev],nums[idx-1]
        nums[idx:]=nums[idx:][::-1]
    return nums






if __name__=='__main__':
    nums=[1,2,3,4,5,3,5,4]
    print(per(nums))