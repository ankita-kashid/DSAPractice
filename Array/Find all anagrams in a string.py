"""
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""
from collections import Counter
def anag(s,p):
    m=len(p)-1
    pc=Counter(p)
    sc=Counter(s[:m])
    res=[]
    for i in range(m,len(s)):
        sc[s[i]]+=1
        if pc==sc:
            res.append(i-len(p)+1)
        sc[s[i-len(p)+1]]-=1
    return res







print(anag("cbaebabacd","abc"))