# # Check Palindrome
# s = 'mom'
# rs =''
# for i in s:
#     rs += i
# if s == rs:
#     print(True)
# else:
#     print(False)


# # Check Palindrome
# def palindrome(s):
#     left = 0
#     right = len(s)-1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left +=1
#         right -=1
#     return True
# print(palindrome("madam"))



# # palindrome using recursion
# def palindrome(s,l,r):
#     if l >= r and s[l] == s[r]:
#         return True
#     if s[l] != s[r]:
#         return False
#     return palindrome(s,l+1,r-1)

# s = "madam"
# l = 0
# r = len(s)-1
# # palindrome(s,l,r)
# print(palindrome(s,l,r))




# # Find the febonacci number 
# def febunachi(self,x):
#     if x == 0 or x == 1:
#         return x
#     return febunachi(x-1) + febunachi(x-2)


# a=febunachi(9)
# print(a)