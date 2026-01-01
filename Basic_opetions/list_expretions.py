# # find largesr number of an array
# def largest(num):
#     larg = num[0] # or large = float("-inf")
#     for i in range(len(num)):
#         if num[i]>larg:
#             larg = num[i]
#     return larg
# print(largest([-3,-5,-9,-1,-6]))



# # find second largest element of array (better solution)
# def largest(num):
#     first_larg = num[0] # or large = float("-inf")
#     for i in range(len(num)):
#         if num[i]>first_larg:
#             first_larg = num[i]

#     sec_larg = float("-inf")
#     for j in range(len(num)):
#         if num[j]> sec_larg and num[j] != first_larg:
#             sec_larg = num[j]
#     return sec_larg
# print(largest([3,5,9,1,6]))



# # find second largest element of array (optimal solution)
# def largest(num):
#     f_larg = float("-inf")
#     s_larg = float("-inf")
#     for i in range(len(num)):
#         if num[i]> f_larg:
#             s_larg = f_larg
#             f_larg = num[i]
#         elif num[i] > s_larg and num[i] != f_larg:
#             s_larg = num[i]
#     return s_larg
# print(largest([3,5,9,1,6]))




# # check if array is sorted or not return true or false
# def check(arr):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             return False
#     return True

# print(check([1,2,3,4,5]))




# # remove dublicate and return total unique elements
# def removed(arr):
#     i = 0
#     j = i +1
#     n = len(arr)
#     if n == 1:
#         return 1
#     while j < n: 
#         if arr[j] != arr[i]:
#             i+=1
#             arr[j], arr[i] = arr[i], arr[j]
#         j +=1
#     return f"Unique elements are {i+1}"
# print(removed([1,1,1,3,4,4,2,5,8,9,9]))




# # right rorate array by 1 place with slicing
# def rotate(arr):
#     n = len(arr)
#     arr[:] = [arr[-1]] + arr[:n-1] # [:] using this not create new array
#     return arr
# print(rotate([1,2,3,4,5]))



# # right rorate array by 1 place without slicing
# def rotate(arr):
#     n = len(arr)
#     tem = arr[n-1]
#     for i in range(n-2,-1,-1):
#         arr[i+1] = arr[i]
#     arr[0] = tem
#     return arr
# print(rotate([1,2,3,4,5]))




# # right rotate array by k places (brote force solution) [In Place]
# def rotate(arr,k):
#     n = len(arr)
#     rotations = k % n
#     for _ in range(rotations):
#         e = arr.pop()
#         arr.insert(0,e)
    
#     return arr

# print(rotate([1,2,3,4,5,6],3))





# # right rotate array by k places using slicing (bater solution) [In Place]
# def rotate(arr,k):
#     n = len(arr)
#     r = k % n
#     arr[:] = arr[n-r:] + arr[:n-r]
#     return arr

# print(rotate([1,2,3,4,5,6],2))





# # right rotate array by k places using slicing (optimal solution) [In Place]
# def rotate(arr,left, right):
#     n = len(arr)
#     while left<right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left+=1
#         right-=1
#     return arr
# a = [1,2,3,4,5,6,7,8]
# k = 3
# n = len(a)
# print(a)
# print(rotate(a,n-k,n-1))
# print(rotate(a,0,n-k-1))
# print(rotate(a,0,n-1))







# # move zeroes to the end [in place] my code
# def move(arr):
#     n = len(arr)
#     for i in range(n):
#         if arr[i] == 0:
#             arr.remove(arr[i])
#             arr.append(0)
#     return arr
# a = [1,0,8,3,0,7,8,6,0,0,5,3,5]
# print(move(a))






# # # move zeroes to the end [in place] (brute force solution)
# def zeros(arr):
#     n = len(arr)
#     temp = []
#     for i in range(n):
#         if arr[i] != 0:
#             temp.append(arr[i])
#     nz = len(temp)
#     for j in range(nz):
#         arr[i] = arr[j]
#     for _ in range(nz,n):
#         arr[i] = 0
#     return arr
# a = [1,0,8,3,0,7,8,6,0,0,5,3,5]
# print(zeros(a))



# # move zeroes to the end [in place] (optimal solution)
# def zeros(arr):
#     if len(arr) == 1:
#         return arr
#     i = 0
#     j = i+1
#     while i <len(arr):
#         if arr[i] == 0:
#             break
#         i+=1
#     if i == len(arr):
#         return
#     while j < len(arr):
#         if arr[j] != 0:
#             arr[j], arr[i] = arr[i], arr[j]
#             i+=1
#         j+=1
#     return arr
# a = [1,0,2,0,3,4,0,5]
# print(zeros(a))





# # linear search 
# def linear(arr,target):
#     n = len(arr)
#     for i in range(n):
#         if arr[i] == target:
#             return i
#     return -1
# a = [1,2,3,4,5,6,7,8,7]
# print(linear(a,7))





# # merge two sorted arrays but duplicate are not alowed
# def two_list(arr1,arr2):
#     n,m = len(arr1)-1, len(arr2)-1
#     result = []
#     i = j = 0
#     while i < n and j < m:
#         if arr1[i] <= arr2[j]:
#             if len(result)==0 or arr1[i] != result[-1]:
#                 result.append(arr1[i])
#             i+=1
#         else:
#             if len(result)==0 or arr2[j] != result[-1]:
#                 result.append(arr2[j])
#             j+=1
#     while i < n:
#         if len(result)==0 or arr1[i] != result[-1]:
#             result.append(arr1[i])
#         i+=1
#     while j < m:
#         if len(result)==0 or arr2[j] != result[-1]:
#             result.append(arr2[j])
#         j+=1
#     return result
# a = [1,1,2,3,4,5]
# b = [2,2,2,4,5,6,7,8,9]
# print(two_list(a,b))






# # find missing numbar of array (brute force solution)
# def missing(arr):
#     n = len(arr)
#     for i in range(n+1):
#         if i not in arr:
#             return i

# a = [1,2,3,4,0]
# print(missing(a))







# # find missing numbar of array (better solution)
# def missing(arr):
#     n = len(arr)
#     dic = {}
#     for i in range(n+1):
#         dic[i] = 0
#     for j in range(n):
#         if arr[j] in dic:
#             dic[arr[j]] +=1
#     for key, value in dic.items():
#         if value == 0:
#             return key
# a = [1,2,3,4,8,6,9,0]
# print(missing(a))




# # # find missing numbar of array (optimal solution)
# def missing(arr):
#     n = len(arr)
#     tem = 0
#     a = 0
#     for i in range(n+1):
#         tem += i
#     for j in range(n):
#         a += arr[j]
#     return tem-a

# a = [1,2,3,4,5,6,0,8,9,10]
# print(missing(a))





# # maximum consecutive ones (optimal solution)
# def consecute(arr):
#     n = len(arr)
#     count = 0
#     max_count = 0
#     for i in range(n):
#         if arr[i] == 1:
#             count +=1
#         else:
#             max_count = max(max_count, count)
#             count=0
#     return max(max_count,count)
# a = [1,1,0,1,1,1,0,1,0]
# print(consecute(a))

