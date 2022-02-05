"""
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
output = [1,9,8,4,2,7,6,9,0,0,0,0]
"""
def zero(nums):
    count=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[count]=nums[i]
            count+=1
    while count<len(nums):
        nums[count]=0
        count+=1
    return nums 
    

# Method 2:
def zer02(nums):
    i=0
    j=1
    while(j<len(nums)):
        # print(nums)
        if nums[i]==0 and nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
        elif nums[i]==0 and nums[j]==0:
            j+=1
        else:
            i+=1
            j+=1
    return nums
        

if __name__=='__main__':
    nums=[1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    print(zer02(nums))