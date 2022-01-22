def pair(nums,t):
    dic={}
    count=0
    for i in range(len(nums)):
        if t-nums[i] in dic:
            count+=dic[t-nums[i]]
        if nums[i] in dic:
            dic[nums[i]]+=1
        else:
            dic[nums[i]]=1

    return count

if __name__=='__main__':
    nums=[1,2,3,2,4,1]
    target=5
    print(pair(nums,target))