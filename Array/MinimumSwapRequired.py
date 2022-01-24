"""
arr = [2, 1, 5, 6, 3]
k=3
"""
def cswaps(nums,i,j,pivot):
    c=0
    for k in nums:
        if k< pivot:
            c+=1
    nums[i+c],nums[i]=nums[i],nums[i+c]

    start=i
    end=j
    count=0
    print(start,end)
    while start<=end:
        if nums[start]<=pivot:
            start+=1
        elif nums[end]>pivot:
            end-=1
        else:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
            count+=1
        print(nums,start,end)
    return count

def swaps(nums,k):
    return cswaps(nums,0,len(nums)-1,k)

if __name__=='__main__':
    nums= [2, 7, 9, 5, 8, 7, 4]
    k=5
    print(swaps(nums,k))