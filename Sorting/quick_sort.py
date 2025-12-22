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

def partition(num,low, high):
    pivot = num[low]
    i, j = low, high
    while i < j:
        while num[i] <= pivot and i <= high-1:
            i+=1
        while num[j] >= pivot and j >= low+1:
            j-=1
        if i < j:
            num[i], num[j] = num[j], num[i]
    num[low], num[j] = num[j], num[low]
    return j
    

def quick(num,low,high):
    if low < high:
        partition(num,low,high)
        quick(num,low,high-1)
        quick(num,low+1,high)
    return num


a = [10, 7, 8, 9, 1, 5]
s = quick(a,0,len(a)-1)
print(s)