

import copy

def zero_matrix(m):
    
    mz = copy.deepcopy(m)
    
    r = len(m)
    c = len(m[0])
    
    for i in range(r):
        for j in range(c):
            if m[i][j] == 0:
                for x in range(r):
                    mz[x][j] = 0
                for y in range(c):
                    mz[i][y] = 0
                
    return mz



m = [[0, 1, 2, 3], [2, 3, 0, 4], [1, 2, 3, 4]]

print(zero_matrix(m))