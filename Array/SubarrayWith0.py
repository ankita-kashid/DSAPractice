

def sum0(nums):
    s=set()
    sum=0
    for i in nums:
        sum+=i
        if sum==0 or sum in s:
            return True
        s.add(i)
    return False

if __name__=='__main__':
    nums=[4,2,-3,1,6]
    print(sum0(nums))