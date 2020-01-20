
# Runtime O(n^2) for both average and worst case.
# Memory O(1)


def bubble_sort(array):
    swaps = 0
    while(1):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                swaps = swaps + 1
        if swaps == 0:
            break
        else:
            swaps = 0
    
    
array = [2, 4, 1, 3, 5, 9, 7, 6]
bubble_sort(array)