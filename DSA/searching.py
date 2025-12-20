# # linear search
# arr = [10,20,30,40,50,60,70,80,90]
# target = 20

# for i in range(len(arr)):
#     if target == arr[i]:
#         print(f"Target {target} found at position {i}")
#     elif target not in arr:
#         print(None)
#         break



# binary search
arr = [10,20,30,40,50,60,70,80,90]
target = 20
left = 0
right = len(arr)

try:  
    while left <= right:
        mid = (left + right) // 2
        if target not in arr:
            print(None)
            break
        if arr[mid] == target:
            print(f"Target {target} found at position {mid}")
            break
        elif target < arr[mid]:
            right = mid -1
        else:
            left = mid +1
except:
    print(IndexError)
