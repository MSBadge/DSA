## breack recursion in function (head recursion)
# count = 0
# def fuc():
#     global count # to call globle variable in function use globle keyword
#     if count == 4:
#         return
#     print("Head")
#     count += 1
#     fuc()
# fuc()





## Tail recursion
# count = 0
# def fuc():
#     global count # to call globle variable in function use globle keyword
#     if count == 4:
#         return
#     # print("Head")
#     count += 1
#     fuc()
#     print("Tail")
# fuc()





# # recursion with parameter
# def fuc(a,b):
#     a, b = a, b
#     if b == 0:
#         return
#     print(a)
#     b -= 1        # decrese value
#     fuc(a,b)
# x = 'mukul'       # what print
# t = 4             # how many time
# fuc(x,t)




# # recursion with parameter
# def fuc(x,n):
#     if n > 4:
#         return
#     print(x)    # head recursion
#     n += 1      # increse value
#     fuc(x,n)
#     print('tail')   # tail recursion
# fuc('mukul',1)


# parametrize recursion
# def fuc(some,i,n):
#     if i > n:
#         print(some)   # when we use print it is parametrize
#         return
#     fuc(some+i,i+1,n)
#     print(i)
# fuc(0,1,4)


# # functional recursion
# def fun(n):
#     if n == 1:
#         return 1        # when we return it is functional
#     print(n)
#     return n + fun(n-1)
# print(fun(4))



# # factorial of number using recursion
# def fun(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * fun(n-1)

# print(fun(5))




# # reverce an array using recursion
# def fun(x,l,r):
#     x[l], x[r] = x[r], x[l]
#     if l >= r :
#         return
#     fun(x,l+1,r-1)

# def rev(a,l,r):
#     fun(a,l,r)
#     return a

# a = [5,7,3,9,1,5,7,0,8]
# l = 2             # perticular position reverce
# r = 7
# print(rev(a,l,r))        # o/p: [5, 7, 0, 7, 1, 5, 9, 3, 8]




# # reverce using while loop
# a = [5,7,3,9,1,5,7,0,8]
# l = 1             # perticular position reverce
# r = 2
# rev = a
# print(f"Before change: {a}")
# while l < r:
#     a[l], a[r] = a[r], a[l]
#     l += 1
#     r -= 1
#     if l >= r:
#         break

# print(f"After change: {a}")
