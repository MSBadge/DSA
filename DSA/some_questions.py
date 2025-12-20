# # count charector of string
# s = "mukul"
# dic = {}

# for ch in s:
#     if ch in dic:
#         dic[ch]+=1
#     else:
#         dic[ch]=1
# print(dic)



# # reverce string
# s = "mukul"
# rs = ""
# for i in range(len(s)-1,-1,-1):
#     rs += s[i]
# print(rs)




# # Find Maximum Number in list
# l = [11,5,2,56,9]
# mnum = l[0]
# for num in l:
#     if num > mnum:
#         mnum = num
# print(mnum)




# Check Palindrome
# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1
    
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# # Test
# print(is_palindrome("racecar"))  # Output: True
# print(is_palindrome("hello"))    # Output: False




# # Remove Duplicates from List
# l = [2,6,7,1,2,4,6,7]
# r = []
# for i in l:
#     if i not in r:
#         r.append(i)
# print(l)
# print(r)




# # Find Factorial
# def factorial(n):
#     num = n
#     fac = []
#     for i in range(1,n//2+1): # divide n/2 because no need to iterate remening loop, there are not any factorial present
#         if num % i == 0:
#             fac.append(i)
#     fac.append(n)
#     return f"Factorial of {num} : {fac}"

# o = factorial(100)
# print(o)





# # Check Prime Number
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(17))
# print(is_prime(15))





#  Fibonacci Sequence
# feb = [0,1]
# for i in range(2, 20):
#     next_feb = feb[i-1] + feb[i-2]
#     feb.append(next_feb)

# print(feb)




# Bubble Sort (Shorting Algorithm)
# lis = [64, 34, 25, 12, 22, 11, 90]
# n = len(lis)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if lis[j] > lis[j+1]:
#             lis[j], lis[j+1] = lis[j+1], lis[j]
# print(lis)# Output: [11, 12, 22, 25, 34, 64, 90] 


