
#input = [1, 2, 3, 4, 5, 6, 7]
#output= 4 5 6 7 1 2 3 
def rev(nums,i,j):
    while i<j:
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        i+=1
        j-=1

def leftrotate(nums,k):
    if k==0:
        return
    n=len(nums)
    k=k%len(nums)
    rev(nums,0,n-1)
    rev(nums,0,k-1)
    rev(nums,k,n-1)
    #print(nums)

def pri(nums):
    for i in range(0,len(nums)):
        print(nums[i],end=" ")


if __name__=='__main__':
    nums=[1, 2, 3, 4, 5, 6, 7]
    k=4
    leftrotate(nums,k)
    pri(nums)
 