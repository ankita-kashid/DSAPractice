"""n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}"""

def common(a,b,c):
    n1=len(a)
    n2=len(b)
    n3=len(c)
    i,j,k=0,0,0
    while i<n1 and j<n2 and k<n3:
        if a[i]==b[j]==c[k]:
            print(a[i],end=" ")
            i+=1
            j+=1
            k+=1
        elif a[i]<b[j]:
            i+=1
        elif b[j]<c[k]:
            j+=1
        else:
            k+=1





if __name__=='__main__':
    a=[1, 5, 10, 20, 40, 80]
    b=[6, 7, 20, 80, 100]
    c=[3, 4, 15, 20, 30, 70, 80, 120]
    common(a,b,c)