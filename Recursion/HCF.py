#RELATION BETWEEN LCM AND HCF
# A*B =LCM(A,B)*HCF(A,B)

def hcf(a,b):
    if a==0:
        return b
    return hcf(b%a,a)

if __name__=='__main__':
    a=15
    b=20
    print(hcf(15,20))