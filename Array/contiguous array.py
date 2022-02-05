def contiguous(nums):
    for i in range(len(nums)):
        if nums[i]==0:
            nums[i]=-1
    dic={}
    ans=0
    curr_sum=0
    for i in range(len(nums)):
        curr_sum+=nums[i]
        if curr_sum == 0:
            ans=i+1
        if curr_sum in dic:
            ans=max(ans,i-dic[curr_sum])
        else:
            dic[nums[i]]=i
    return ans

print(contiguous([1,1,1,1]))