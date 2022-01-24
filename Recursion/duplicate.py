#Remove consecutive duplicate from the strings
#input = "baabacgffh"
#output = "babacgfh"

def dupi(s):
    if len(s)<=2:
        return s
    elif s[0]!=s[1]:
        return s[0]+dupi(s[1:])
    return dupi(s[1:])

if __name__=='__main__':
    string="baabacgffh"
    print(dupi(string))