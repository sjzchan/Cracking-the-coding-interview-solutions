

def binary_search(array, x):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) / 2
        if array[mid] < x:
            low = mid + 1
        
        elif array[mid] > x:
            high = mid - 1
        
        else:
            return mid
    
    return -1   # Error


def binary_search_recursive(array, x, low, high):
    if low > high:
        return -1   # Error
    
    mid = (low + high) / 2
    
    if array[mid] < x:
        return binary_search_recursive(array, x, mid+1, high)
    
    elif array[mid > x]:
        return binary_search_recursive(array, x, low, mid-1)
    
    else:
        return mid
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    