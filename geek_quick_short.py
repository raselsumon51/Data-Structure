# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, low, high):

	# Choose the rightmost element as pivot
	pivot = array[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

def quicksort(array, low, high):
    if low < high:
        print(f'recursion 1: low: {low} high: {high}')  # Corrected indentation
        # Find pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partition(array, low, high)  # Corrected indentation
        print(f'pi: {pi} result: {array}')  # Corrected indentation
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)  # Corrected indentation

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)  # Corrected indentation


# Driver code
if __name__ == '__main__':
	array = [9,-3,5,2,6,8,-6,1,3]
	N = len(array)

	# Function call
	quicksort(array, 0, N - 1)
	print('Sorted array:')
	for x in array:
		print(x, end=" ")

# This code is contributed by Adnan Aliakbar


