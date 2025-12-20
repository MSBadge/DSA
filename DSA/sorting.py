# # Bubble Sort
# arr = [8, 5, 9, 3, 2, 6]
# n = len(arr)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             print(arr)
#     print("------------------")



     
# Sellection Sort
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_value = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_value]:
#                 min_value = j

#         arr[i], arr[min_value] = arr[min_value], arr[i]
#     return arr


# arr = [32, 56, 44, 12, 23]
# s=selection_sort(arr)
# print(s)





# Insertion sort
# arr = [5,4,3,1,2]
# n = len(arr)
# print(arr)
# for i in range(1, n):
#     j = i
#     while arr[j-1] > arr[j] and j > 0:
#         arr[j], arr[j-1] = arr[j-1], arr[j]
#         j -=1
#     print(arr)




# Quick sort
# arr = [79,12,46,35,86,92,53]
# def quick_sort(arr):
#     n = len(arr)
#     if n <= 1:
#         return arr
    
#     pivot = arr[n // 2]  # Choose middle element as pivot
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
    
#     return quick_sort(left) + middle + quick_sort(right)

# # Example
# numbers = [10, 7, 8, 9, 1, 5]
# print("Quick Sort:", quick_sort(numbers.copy()))
# # Output: [1, 5, 7, 8, 9, 10]


# Merge Sort

def merge_sort_array(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left_hand = arr[:mid]
    right_hand = arr[mid:]

    left_sort = merge_sort_array(left_hand)
    right_sort = merge_sort_array(right_hand)

    return merge_array(left_sort, right_sort)

def merge_array(left, right):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        while i < len(left):
            result.append(left[i])
            i += 1
    if j < len(right):
        while j < len(right):
            result.append(right[j])
            j += 1
    return result


arr = [12, 56, 32, 85, 16, 45, 74]
a = merge_sort_array(arr)
print(a)