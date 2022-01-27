count=0
def conso(st):
    global count
    if len(st)==0:
        return count
    if st[0] not in ["a","A","E","e","o","O","i","I","u","U"]:
        count+=1
    
    return conso(st[1:])

print(conso("Amit"))