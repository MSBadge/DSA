# # count integer value
# def count(num):
#     n = num
#     co = 0
#     while n > 0:
#         co += 1
#         n = n //10
#     return co
# print(count(158))



# # 2nd way to count number of integer using log
# from math import *
# def count(num):
#     return int(log10(num)+1)
# print(count(158))



# # check palindrom of integer
# def check(num):
#     n = num
#     rs = 0
#     while n > 0:
#         ld = n % 10
#         rs = rs *10 + ld
#         n = n // 10
#     return num == rs
# print(check(1212))



# # Armstron number integer
# def armstrong(num):
#     n = num
#     node = len(str(num))
#     result = 0
#     while n > 0:
#         ld = n % 10
#         result += ld**node
#         n = n // 10
#     return result == num
# print(armstrong(1634))



# # Armstron number of string
# def starm(num):
#     n = int(num)
#     node = len(num)
#     result = 0
#     while n > 0:
#         ld = n % 10
#         result += ld**node
#         n = n // 10
#     return str(result) == num
# print(starm("153"))



# # Factorial or Divisor 1
# def factorial(num):
#     fa = []
#     for i in range(1,num//2+1):
#         if num % i ==0:
#             fa.append(i)
#     fa.append(num)
#     return fa

# print(factorial(36))



# # Factorial or Divisor 2
# def facto(num):
#     f = []
#     for i in range(1,num+1):
#         if num % i == 0:
#             f.append(i)

#     return f

# print(facto(36))



# # Factorial or Divisor 3
# from math import sqrt
# def fac(num):
#     n = sqrt(num)
#     result = []
#     for i in range(1,int(n)+1):
#         if num % i == 0:
#             result.append(i)
#             if num // i != i:
#                 result.append(num//i)
#     return result
# print(fac(36))



# # friquency map or dictionary
# a = [4,4,7,7,8,6,2,4,7,8,0,6,3,14,7]
# def friq(num):
#     dic = {}
#     for i in range(len(num)):
#         if num[i] in dic:
#             dic[num[i]]+=1
#         else:
#             dic[num[i]]=1
#     return dic
# print(friq(a))



# def friquency(li):
#     dic ={}
#     for i in range(len(li)):
#         dic[li[i]] = dic.get(li[i],0)+1
#     return dic

# print(friquency(a))


 
# # Number Hashing 
# n = [4,3,1,7,8,9,3,6,4,7,5,6,2,1,7,5,9,8,7,3]
# m = [1,2,3,4,5,6,7,8,9]

# def strore(n,m):
#     dic = {}
#     for i in range(len(n)):
#         if n[i] <= 10 and n[i]> 0:
#             dic[n[i]] = dic.get(n[i],0)+1
#     for j in range(len(m)):
#         if m[j] in dic:
#             print(f"{m[j]}:{dic[m[j]]}")     
# strore(n,m)



# # String hashing
# n = ['a','a','s','e','f','b','b','b','s']
# m = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# def strore(n,m):
#     dic = {}
#     for i in range(len(n)):
#         if i not in n:
#             dic[n[i]] = dic.get(n[i],0)+1
#     for j in range(len(m)):
#         if m[j] in dic:
#             print(f"{m[j]}:{dic[m[j]]}")     
# strore(n,m)



####################################

