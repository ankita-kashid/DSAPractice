# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
def pattern(p,s):
    d={}
    l=list(s.split())

    if len(p)!=len(l):
        return False
    if len(set(p))!=len(set(l)):
        return False

    for i in range(len(l)):
        if p[i] not in d:
            d[p[i]]=l[i]
        else:
            if d[p[i]]!=l[i]:
                return False
    return True

if __name__=='__main__':
    p="abb"
    s="dog cat cat dog"
    print(pattern(p,s))