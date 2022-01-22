
#nums=[1,2,0,3,4,0]

def pro(nums):
    product=1
    count=0
    for i in range(len(nums)):
        if nums[i]!=0:
            product=product*nums[i]
        if nums[i]==0:
            count+=1
    if count>=2:
        for i in range(len(nums)):
            nums[i]=0
        return nums

    for i in range(len(nums)):
        if count==1 and nums[i]!=0:
            nums[i]=0

        elif count==1 and nums[i]==0:
            nums[i]=product
        else:
            nums[i]=product//nums[i]
    return nums

if __name__=='__main__':
    nums=[1,2,3,4]
    print(pro(nums))