

# Find Common Elements
# li1 = [1,2,3,4]
# li2 = [3,4,5,6]
# commen = []
# for item in li1:
#     if item in li2 and item not in commen:
#         commen.append(item)
# print(commen)  # Output: [3, 4]



# 11. Binary Search
# def binary_search(arr, target):
#     left, right = 0, len(arr)-1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
# li = [10,20,30,40,50]
# b = binary_search(li,60)
# print(b)




# Matrix Multiplication
# def matrix(A,B):
#     row_A = len(A)
#     col_A = len(A[0])
#     row_B = len(B)
#     col_B = len(B[0])
#     print(f"A = [{row_A}x{col_A}]")
#     print(f"B = [{row_B}x{col_B}]")


#     result = [[0 for _ in range(col_B)] for _ in range(row_A)]

#     for i in range(row_A):
#         for j in range(col_B):
#             for k in range(row_B):
#                 result[i][j] += A[i][k] * B[k][j]
#     return result


# A = [[3,1,4]]

# B = [[4,3],
#      [2,5],
#      [6,8]]

# print(matrix(A,B))






# # Palindrome of Integer value
# def palindrome(n):
#     num = n
#     reverse = 0
#     while num > 0:
#         ld = num % 10 
#         reverse = reverse * 10 + ld
#         num = num // 10
#     return n == reverse

# n = 101
# o = palindrome(n)
# print(o)






# # Armstrong Number
# def countNumber(n): # thid function count the length of integer
#     num = n
#     totalNum = 0
#     while num > 0: 
#         totalNum += 1
#         num = num // 10
#     return totalNum
# def armstrong(n): # this function check is armstrong number of not
#     num = n
#     count = countNumber(n)
#     total = 0

#     while num > 0:
#         ld = num % 10
#         total += ld ** count
#         num = num // 10
#     return total == n
# n = 1634 # True
# o = armstrong(n)
# print(o)




# # Find Factorial 2nd case
# def factorial(n):
#     num = n
#     fac = []
#     for i in range(1,n//2+1): # divide n/2 because no need to iterate remening loop, there are not any factorial present
#         if num % i == 0:
#             fac.append(i)
#     fac.append(n)
#     return f"Factorial of {num} : {fac}"

# o = factorial(99)
# print(o)




# # Find factorial 3rd case
# from math import sqrt
# def factorial(num):
#     l = []
#     s = int(sqrt(num))
#     for i in range(1,s+1):
#         if num % i == 0:
#             l.append(i)
#             if num // i != i:
#                 l.append(num//i)

#     l.sort()
#     return l

# print(factorial(36))
