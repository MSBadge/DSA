# # iteration solution
# def binary(arr,target):
#     n = len(arr)
#     low = 0
#     high = n-1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             high = mid-1
#         else:
#             low = mid +1
#     return -1

# a = [1,2,3,4,5,6,7,8,9]
# print(binary(a,10))







# # recursion solution
# def search(arr,low,high,target):
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return search(arr,mid+1,high,target)
#     else:
#         return search(arr,low,mid-1,target)

# a = [1,2,3,4,5,6,7,8,9]
# low = 0
# high = len(a)-1
# print(search(a,low,high,2))










# # Lower Bound (smallest index such that nums[i]>=target)
# def lowerBound(nums,target):
#     n = len(nums)
#     lb = n
#     low = 0
#     high = n-1
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] >= target:
#             lb = mid
#             high = mid-1
#         else:
#             low = mid+1
#     return lb

# a = [1,1,1,2,3,3,4,5,6,7,7,7,8,9]
# print(lowerBound(a,20))


 




# # upper Bound (smallest kndex such that nums[i]>=target)
# def upperBound(nums,target):
#     n = len(nums)
#     left = 0
#     right = n-1
#     upper_bound = n
#     if target not in nums:
#         return -1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] <= target:
#             upper_bound = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     return upper_bound
# a = [1,1,1,2,3,3,4,5,6,7,7,7,8,9]
# print(upperBound(a,1))










# # search insert position (optimal solution)
# def search(nums,target):
#     n = len(nums)
#     low = 0
#     high = n -1
#     lb = n
#     while low <= high:
#         mid = (low+high)//2
#         if nums[mid] >= target:
#             lb = mid
#             high = mid-1
#         else:
#             low = mid+1
#     return lb

# a = [1,2,4,5,6,8,9]
# print(search(a,7))







# # ceil the floor (optimal)
# def ceilFloor(nums,target):
#     n = len(nums)
#     low = 0
#     high = n-1
#     cail = floor = -1
#     while low <= high:
#         mid = (low + high)//2
#         if nums[mid] == target:
#             return [nums[mid],nums[mid]]
#         elif nums[mid] > target:
#             cail = nums[mid]
#             high = mid-1
#         else:
#             floor = nums[mid]
#             low = mid+1
#     return [floor,cail]

# a = [1,2,4,5,6,8,9]
# print(ceilFloor(a,3))





# # first and last occurence 
# def firstOccurence(nums,target):
#     n = len(nums)
#     left = 0
#     right = n-1
#     lowerBound = n
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] >= target:
#             lowerBound = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#     return lowerBound

# def lastOccurence(nums,target):
#     n = len(nums)
#     left = 0
#     right = n-1
#     upper_bound = n
#     if target not in nums:
#         return -1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] <= target:
#             upper_bound = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     return upper_bound

# def occurence(nums, target):
#     lowerbound = firstOccurence(nums,target)
#     upperbound = lastOccurence(nums, target)
            
#     return [lowerbound,upperbound]

# a = [1,2,3,3,3,3,4,5]
# print(occurence(a,3))







# # count occurrences of a numbar in a sorted array with duplicates
# def count(nums,target):
#     n = len(nums)
#     left = 0
#     right = n -1
#     lb = n 
#     count = 0
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] >= target:
#             lb = mid

#             right = mid-1
#         else:
#             left = mid+1
#     for i in range(lb,n):
#         if nums[lb] == nums[i]:
#             count+=1
#         else:
#             break
#     return count

# a = [1,2,3,3,3,3,4,5]
# print(count(a,3))








# # search in rotated sorted array I
# def search(arr,target):
#     n = len(arr)
#     left, right = 0, n-1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         if arr[mid] <= arr[right]:
#             if arr[mid] <= target <= arr[right]:
#                 left = mid+1
#             else:
#                 right = mid-1
#         else:
#             if arr[left] <=target <= arr[mid]:
#                 right = mid-1
#             else:
#                 left = mid+1
#     return -1

# a = [9,8,1,2,3,4,5,6,7]
# print(search(a,4))







# # search in rotated sorted array II
# def search(arr,target):
#     n = len(arr)
#     left, right = 0, n-1

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return True
        
#         if arr[mid] == arr[left] == arr[right]:
#             left +=1
#             right -=1
#             continue

#         if arr[left] <= arr[mid]:
#             if arr[left] <= target <= arr[mid]:
#                 right = mid-1
#             else:
#                 left = mid+1
#         else:
#             if arr[mid] <= target <= arr[right]:
#                 left = mid+1
#             else:
#                 right = mid-1
         
#     return False

# a = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
# print(search(a,2))







# # find minimum in rotated sorted array
# def find(nums):
#     n = len(nums)
#     left, right = 0, n-1
#     rotation = float("inf")

#     while left <= right:
#         mid = (left + right) // 2

#         if nums[mid] <= nums[right]:
#             rotation = min(rotation,nums[mid])
#             right = mid-1
#         else:
#             left = mid +1
        
        
    
#     return rotation

# nums = [3,4,5,6,1,2]
# print(find(nums))



