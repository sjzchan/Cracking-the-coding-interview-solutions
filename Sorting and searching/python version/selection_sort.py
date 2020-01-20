
# Runtime O(n^2) for both average and worst case.
# Memory O(1)

def selection_sort(array):
    
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

    
    
array = [2, 4, 1, 3, 5, 9, 7, 6]
selection_sort(array)