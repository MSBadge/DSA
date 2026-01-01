# # 3 sum problem (brute solution)
# def threesum(arr):
#     n = len(arr)
#     my_set = set()
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if arr[i]+arr[j]+arr[k] == 0:
#                     tem = [arr[i],arr[j],arr[k]]
#                     tem.sort()
#                     my_set.add(tuple(tem))
#     return [list(ans) for ans in my_set]
# nums = [-1,0,1,2,-1,-4]
# # Output: [[-1,-1,2],[-1,0,1]]
# print(threesum(nums))








# # 3 sum problem (better solution)
# def threesum(arr):
#     n = len(arr)
#     result = set()
#     for i in range(n):
#         my_set = set()
#         for j in range(i+1,n):
#             third = -(arr[i] + arr[j])
#             if third in my_set:
#                 tem = [arr[i],arr[j],third]
#                 tem.sort()
#                 result.add(tuple(tem))
#             my_set.add(arr[j])
#     return [list(ans) for ans in result]
# nums = [-1,0,1,2,-1,-4]
# # Output: [[-1,-1,2],[-1,0,1]]
# print(threesum(nums))








# # 3 sum problem (optimal solution)
# def threesum(arr):
#     arr.sort()
#     n = len(arr)
#     result = []
#     for i in range(n-2):
#         if i != 0 and arr[i] == arr[i-1]:
#             continue
#         j = i + 1
#         k = n - 1
#         while j < k:
#             total = arr[i] + arr[j] + arr[k]
#             if total == 0:
#                 result.append([arr[i], arr[j], arr[k]])
#                 while j < k and arr[j] == arr[j+1]:
#                     j+=1
#                 while j < k and arr[k] == arr[k-1]:
#                     k-=1
#                 j+=1
#                 k-=1
#             elif total < 0:
#                 j+=1
#             else:
#                 k-=1    
#     return result
# nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
# print(threesum(nums))









# 4 sum Problem (my code)
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


# def fourSum(arr, target):
#     arr.sort()
#     n = len(arr)
#     if n < 4:
#         return []
#     result = []
#     for i in range(n-3):
#         j = i+1
#         for k in range(n-1,-1,-1):
#             l = k-1
#             while j < l:
#                 total = arr[i] + arr[j] + arr[k] + arr[l]
#                 if total == target:
#                     ans = [arr[i], arr[j], arr[k], arr[l]]
#                     ans.sort()
#                     if ans not in result:
#                         result.append(ans)
#                     while j < l and arr[j] == arr[j+1]:
#                         j+=1
#                     while j < l and arr[k] == arr[k-1]:
#                         k-=1
#                     j+=1
#                     l-=1
#                 elif total > target:
#                     if j >= l:
#                         j+=1
#                     l-=1
#                 else:
#                     j+=1
#     return result

# nums = [-3,-1,0,2,4,5]
# target = 2

# print(fourSum(nums,target))









# # 4 Sum (optimal solution)
# def fourSum(arr,target):
#     n = len(arr)
#     nums.sort()
#     result = []
#     for i in range(n-3):
#         if i > 0 and arr[i] == arr[i-1]:
#             continue
#         for j in range(i+1,n-2):
#             if j > i+1 and arr[j] == arr[j-1]:
#                 continue
#             k = j+1
#             l = n-1
#             while k < l:
#                 total = arr[i] + arr[j] + arr[k] + arr[l]
#                 if total == target:
#                     ans = [arr[i], arr[j], arr[k], arr[l]]
#                     result.append(ans)
#                     while k < l and arr[k] == arr[k+1]:
#                         k+=1
#                     while k < l and arr[l] == arr[l-1]:
#                         l-=1
#                     k+=1
#                     l-=1
#                 elif total < target:
#                     k+=1
#                 else:
#                     l-=1
#     return result
# nums = [1,0,-1,0,-2,2]
# target = 0
# print(fourSum(nums,target))










