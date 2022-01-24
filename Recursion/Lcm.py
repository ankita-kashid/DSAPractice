#Relation between hcf and lcm
#a*b = lcm(a,b)*hcf(a,b)
def hcf(a,b):
    if a==0:
        return b
    return hcf(b%a,a)

def lcm(a,b):
    return a*b//hcf(a,b)

if __name__=='__main__':
    a=15
    b=20
    print(lcm(a,b))
