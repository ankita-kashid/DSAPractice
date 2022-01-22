"""Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]"""

def triplet(n,t):
    n.sort()
    out=[]
    for i in range(len(n)):
        l=i+1
        r=len(n)-1
        x=n[i]
        while l<r:
            if x+n[l]+n[r]==t:
                if x+n[l]+n[r] not in out:
                    out.append([x,n[l],n[r]])
                l+=1
                r-=1
            elif x+n[l]+n[r]<t:
                l+=1
            else:
                r-=1
    return out




if __name__=='__main__':
    nums=[1 ,4 ,45 ,6 ,10 ,8]
    target=13
    print(triplet(nums,target))