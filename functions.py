######### Menu options below #########
def main_menu():
    print("Select the sorting algorithm you want to test.\n\
          ---------------------------\n\
          1. Bubble Sort\n\
          2. Merge Sort\n\
          3. Quick Sort\n\
          4. TBD\n\
          5. Exit\n\
          Select a sorting algorithm (1-5): ")
    
def bbl_menu():
    print("\nCase Scenarios for Bubble Sort\n\
          -----------------\n\
          1. Best Case\n\
          2. Average Case\n\
          3. Worst Case\n\
          4. Exit bubble sort test")
    
def merge_menu():
    print("\nCase Scenarios for Merge Sort\n\
          -----------------\n\
          1. Best Case\n\
          2. Average Case\n\
          3. Worst Case\n\
          4. Exit merge sort test")
    
def quick_menu():
    print("\nCase Scenarios for Quick Sort\n\
          -----------------\n\
          1. Best Case\n\
          2. Average Case\n\
          3. Worst Case\n\
          4. Exit quick sort test")
    
def tbd_menu():
    print("\nCase Scenarios for tbd Sort\n\
          -----------------\n\
          1. Best Case\n\
          2. Average Case\n\
          3. Worst Case\n\
          4. Exit tbd sort test")
################################################

'''
Generates a list of random numbers to be sorted by a sorting algorithm
Parameters
    size: The amount of numbers to generate
    floor: The lower bound of the number generator
    ceiling: The upper bound of the number generator
Returns
    nums: The list of random numbers
'''
import random
def generate_nums(size = 1, floor = 1, ceiling = 1_000):
    nums = []

    for i in range(0, size):
        nums.append(random.randrange(floor, ceiling))

    return nums

######### Sorting Algorithms below #########
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted, so skip them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def merge_sort(arr):
    # Base case: if the list is a single element, it is already sorted
    if len(arr) > 1:
        
        # Find the middle of the array
        mid = len(arr) // 2
        
        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the sorted halves
        i = j = k = 0
        
        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Check if any element was left in the left_half[]
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Check if any element was left in the right_half[]
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def quick_sort(arr):
    # Base case: if the list has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (here, we use the last element as the pivot)
    pivot = arr[len(arr) - 1]
    
    # Partition the array into two halves: one with elements smaller than pivot, one with elements larger
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively apply quick_sort to the left and right partitions, and concatenate the result with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)
############################################################

