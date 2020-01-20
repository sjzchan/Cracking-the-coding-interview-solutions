

def is_rotation(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    if s1 == s2:
        return True
    
    for i in range(len(s1)):
        s1 = s1[1:] + s1[0:1]
        if s1 == s2:
            return True
    
    return False



s1 = 'waterbottle'
s2 = 'erbottlewat'


print(is_rotation(s1, s2))