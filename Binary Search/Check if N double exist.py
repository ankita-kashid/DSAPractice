#https://leetcode.com/problems/check-if-n-and-its-double-exist/submissions/

def search(nums,x,i):
       # print(x)
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
          #  print(mid)
            if nums[mid]==x and mid!=i :
                #print(nums[mid],"bh")
                return nums[mid]
            elif nums[mid]>x:
                end=mid-1
            else:
                start=mid+1
        return -1
    
    
def checkIfExist(nums):
    nums.sort()
    for i in range(len(nums)-1):
        a=search(nums,nums[i]*2,i)
        
        if a==nums[i]*2:
            return True
    return False

if __name__=='__main__':
    nums=[7,1,14,11]
    print(checkIfExist(nums))
            