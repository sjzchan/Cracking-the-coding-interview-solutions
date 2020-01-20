

import copy

def rotate_matrix(m):
    
    mr = copy.deepcopy(m)
    
    r = len(m)
    c = len(m[0])
    
    for i in range(r):
        for j in range(c):
            mr[i][j] = m[c-1-j][i]
    
    return mr


m = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate_matrix(m))