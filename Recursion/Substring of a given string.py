from re import L


def sub(s,out,l):
    if len(s)==0:
        l.append(out)
        return l
       
    sub(s[1:],out+s[0],l)
    sub(s[1:],out,l)


if __name__=='__main__':
    string="abcab"
    out=""
    l=[]
    a=sub(string,out,l)
    print(l,len(l))