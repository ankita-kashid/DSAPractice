#nums=[2,3,-2,4]
#6

def prod(nums):
    mini=nums[0]
    maxi=nums[0]
    ans=nums[0]
    for i in range(1,len(nums)):
        temp=mini
        mini=min(nums[i],maxi*nums[i],mini*nums[i])
        maxi=max(nums[i],maxi*nums[i],temp*nums[i])
        
        #print(mini,maxi)

        ans=max(ans,maxi)
    return ans

if __name__=='__main__':
    nums=[2,3,-2,4]
    print(prod(nums))