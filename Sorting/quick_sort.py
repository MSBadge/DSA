# Quick sort
def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    pivot = arr[n // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example
numbers = [10, 7, 8, 9, 1, 5]
print("Quick Sort:", quick_sort(numbers.copy()))
# Output: [1, 5, 7, 8, 9, 10]