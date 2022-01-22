def partition(a,si,ei):
    pivot=6  
    #find number of elements smaller than pivot
    c=0
    count=0
    for i in range(si,ei+1):
        if a[i]<pivot:
            c=c+1
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index=si+c
    
    i=si
    j=ei
    while i<j:
        if a[i]<pivot:
            i=i+1
        elif a[j]>=pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
            count+=1
    return count

def quick_sort(a,si,ei): 
    if si>=ei:
        return
    
    pivot_index=partition(a,si,ei)
    return pivot_index
  #  quick_sort(a,si,pivot_index-1)
  #  quick_sort(a,pivot_index+1,ei)
    
   # return


arr=[2, 7, 9, 5, 8, 7, 4]
#print(n,"n",len(arr))
print(quick_sort(arr, 0, len(arr)-1))
#print(a)

