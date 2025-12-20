# selection sort using recursion

# Sellection Sort Assending order
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_value = i
        for j in range(i+1,n):
            if arr[j] < arr[min_value]:
                min_value = j

        arr[i], arr[min_value] = arr[min_value], arr[i]
    return arr


# arr = [32, 56, 44, 12, 23]
# s=selection_sort(arr)
# print(s)

# # Sellection Sort Desending order
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         max_value = i
#         for j in range(i+1,n):
#             if arr[j] > arr[max_value]:
#                 max_value = j

#         arr[i], arr[max_value] = arr[max_value], arr[i]
#     return arr


# arr = [32, 56, 44, 12, 23]
# s=selection_sort(arr)
# print(s)

