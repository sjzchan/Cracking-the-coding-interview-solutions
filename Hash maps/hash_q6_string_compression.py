

def string_compress(s):
    
    char = s[0]
    count = 1
    
    s_out = ''
    
    for i in range(1, len(s)):
        
        if s[i] == char:
            count += 1
        else:
            s_out = s_out + char + str(count)
            count = 1
            char = s[i]
        
        if i == len(s)-1:
            s_out = s_out + char + str(count)
            
    return s_out




s = 'aabcccccaaat'

print(string_compress(s))