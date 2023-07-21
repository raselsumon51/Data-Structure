
def quicksort(arr):
    i=1
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # Select the rightmost element as the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f'pivot: {pivot} left: {left} middle: {middle} right: {right}')

    sorted_left = quicksort(left)
    i=i+1
    print(f'recursion: {i}')
    print(f'Sorted left : {sorted_left}')
    
    sorted_right = quicksort(right)
    print(f'Sorted right : {sorted_right}')
    
    result = sorted_left + middle + sorted_right
    print(f'result : {result}')
    # print(f'Result of quicksort(left) + middle + quicksort(right): {result}')
    return result

# Helper function to keep track of the iteration count
def quicksort_with_iteration_count(arr):
    sorted_arr = quicksort(arr)
    return sorted_arr

# Test the quicksort function with print debugging
arr = [9, -3, 5, 2, 6, 8, -6, 1, 3]
print("Original array:", arr)

sorted_arr = quicksort_with_iteration_count(arr)
print("Sorted array:", sorted_arr)
