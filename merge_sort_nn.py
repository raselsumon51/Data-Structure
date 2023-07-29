def merge_sorted_arrays(arr, start_index, mid_index, end_index):
    # Merge two sorted subarrays into a single sorted array
    merged = []  # Create an empty list to store the merged elements
    left_index, right_index = start_index, mid_index + 1  # Initialize indices for the two subarrays

    # Compare elements from both subarrays and add the smaller one to the merged list
    while left_index <= mid_index and right_index <= end_index:
        if arr[left_index] < arr[right_index]:
            merged.append(arr[left_index])  # Add element from the first subarray
            left_index += 1
        else:
            merged.append(arr[right_index])  # Add element from the second subarray
            right_index += 1

    # Add any remaining elements from the first subarray (if any)
    merged += arr[left_index:mid_index + 1]

    # Add any remaining elements from the second subarray (if any)
    merged += arr[right_index:end_index + 1]

    # Copy the merged array back to the original array
    arr[start_index:end_index + 1] = merged

def merge_sort(arr, start_index=0, end_index=None):
    # Merge sort function
    if end_index is None:
        end_index = len(arr) - 1

    # Base case: if the array has one element or is empty, it is already sorted
    if start_index >= end_index:
        return

    mid_index = (start_index + end_index) // 2

    # Recursively sort the left and right halves of the array
    merge_sort(arr, start_index, mid_index)
    merge_sort(arr, mid_index + 1, end_index)

    # Merge the two sorted halves
    merge_sorted_arrays(arr, start_index, mid_index, end_index)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)
