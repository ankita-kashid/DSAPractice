#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
def sqr(nums):
    leng=len(nums)
    ans=[0]*leng
    i,j,k=0,leng-1,leng-1
    while(i<j):
        first,second=abs(nums[i]),abs(nums[j])
        if first < second:
            ans[k]=second**2
            j-=1
        else:
            ans[k]=first**2
            i+=1
        k-=1
    #print(ans)
    return ans




if __name__=='__main__':
    nums=[-4,3,5,6,9]
    print(sqr(nums))