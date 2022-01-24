#arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
#output = 4   -3    5   -1    6   -7    2    8    9
#Approach
"""
1. First move all the negative elements to the starting
2. 
"""

def rearrange(nums):
    k=-1
    #Moving negative elements to the starting of the array
    for i in range(len(nums)):
        if nums[i]<0:
            k+=1
            nums[k],nums[i]=nums[i],nums[k]
    pos=k+1
    neg=0
    n=len(nums)
    #Rearranging the array as first positive element then negative element and so on..
    while pos<n and neg<pos and nums[neg]<0:
        nums[neg],nums[pos]=nums[pos],nums[neg]
        pos+=1
        neg+=2
    print(nums)
    return nums







if __name__=='__main__':
    nums=[-1, 2, -3, 4, 5, 6, -7, 8, 9]
    print(rearrange(nums))