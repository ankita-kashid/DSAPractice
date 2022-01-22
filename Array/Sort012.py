# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def sort012(nums):
    low,mid=0,0
    high=len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[mid],nums[low]=nums[low],nums[mid]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1

        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums





if __name__=='__main__':
    nums=[2,0,2,1,1,0]
    print(sort012(nums))