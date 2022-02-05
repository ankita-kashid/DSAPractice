"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
def rev(nums,i,j):
    while i<j:
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        i+=1
        j-=1



def leftrotate(nums,k):
    n=len(nums)
    if k==0:
        return
    k=k%len(nums)
    rev(nums,0,k-1)
    rev(nums,k,len(nums)-1)
    rev(nums,0,len(nums)-1)
    #print(nums)

def pri(nums):
    for i in range(0,len(nums)):
        print(nums[i],end=" ")




if __name__=='__main__':
    nums=[1, 3,6,11,12,17]
    k=4
    leftrotate(nums,k)
    pri(nums)
