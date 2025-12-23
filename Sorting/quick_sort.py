# # Quick sort
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



# 2nd technique 

def partision(arr,low,high):
    i, j = low, high
    pivot = arr[low]
    while i < j:
        while arr[i]<=pivot and i <= high-1:
            i +=1
        while arr[j]>= pivot and j >= low+1:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick(arr,low,high):
    if low < high:
        pivot= partision(arr,low,high)
        quick(arr,low,pivot-1)
        quick(arr,pivot+1,high)
    return arr

a = [10, 7, 8, 9, 1, 5]
s = quick(a,0,len(a)-1)
print(s)