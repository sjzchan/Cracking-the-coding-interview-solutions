

def one_away(s1, s2):

    diff = abs(len(s1) - len(s2))
    
    if diff > 1:
        return False
    
    
    d = {}
    
    for i in s1:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    for i in s2:
        if i in d.keys():
            d[i] -= 1
    
    if sum(d.values()) == 0:
        return True
    
    if sum(d.values()) != 0 and diff != 0:
        return False
        
    return True



s1 = 'pale'
s2 = 'pales'
s2 = 'palep'

print(one_away(s1, s2))