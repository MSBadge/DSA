# # genarate all binary strings without consecutive one's
# def genarate(n):
#     result = []
#     nums = ["0"]*n

#     def backtrack(index, flag, num, result):
#         if index >= len(num):
#             result.append("".join(num))
#             return
        
#         num[index] = "0"
#         backtrack(index+1, True, num, result)
        
#         if flag == True:
#             num[index] = "1"
#             backtrack(index+1, False, num, result)
#             num[index] = "0"

#     backtrack(0, True, nums, result)
#     return result

# print(genarate(2))








# # Genarate Paranthesis (leetcode 22)
# def genarate(n):
#     br = [""]*(n*2)
#     result = []

#     def backtrack(index, total, br, result):
#         if index >= len(br):
#             if total == 0:
#                 result.append("".join(br))
#             return
#         if total < n:
#             br[index] = "("
#             backtrack(index+1, total+1, br, result)

#         if total > 0:
#             br[index] = ")"
#             backtrack(index+1, total-1, br, result)

#     backtrack(0,0,br,result)
#     return result
# print(genarate(3))









# # Combination sum (leetcode 39)
# class Solution:
#     def combinationSum(self, num, target):
#         result = []

#         def backtrack(index, total, num, subset):
#             if total == target:
#                 result.append(subset[:])
#                 return
#             elif index >= len(num) or total > target:
#                 return
            
#             now = total + num[index]
#             subset.append(num[index])

#             backtrack(index, now, num, subset)
#             now = total
#             subset.pop()
#             backtrack(index+1, now, num, subset)
            
#         backtrack(0,0,num,[])
#         return result

# o = Solution()
# print(o.combinationSum([2,3,6,7], 8))







# # Combination Sum 2 (leetcode 40)
# class Solution:
#     def combinationSum(self, num, target):
#         num.sort()
#         result = []

#         def backtrack(index, total, subset):
#             if total == 0:
#                 result.append(subset[:])
#                 return
#             if total < 0 or index >= len(num):
#                 return
            
#             for i in range(index,len(num)):
#                 if i > index and num[i] == num[i-1]:
#                     continue
#                 if num[i] > total:
#                     break
#                 subset.append(num[i])
#                 summ = total - num[i]
#                 backtrack(i+1, summ, subset)
#                 subset.pop()         
            
#         backtrack(0,target,[])
#         return result

# o = Solution()
# print(o.combinationSum([10,1,2,7,6,1,5], 8))











# # Combination sum 3 (leetcode 216)
# def genarate(k,n):
#     result = []

#     def backtrack(ind, total, subset):
#         if total == n and len(subset) == k:
#             result.append(subset[:])
#             return
#         if total > n or len(subset) > k:
#             return
        
#         for i in range(ind, 10):
#             subset.append(i)
#             j = total + i
#             backtrack(i+1, j, subset)
#             subset.pop()
            

#     backtrack(1,0,[])
#     return result

# print(genarate(2,8))






# # subset sum 1
# def genarate(num):
#     result = []
#     def backtrack(index, total):
#         if index >= len(num):
#             result.append(total)
#             return
        
#         k = total + num[index]
#         backtrack(index+1, k)

#         backtrack(index+1, total)

#     backtrack(0,0)
#     return result

# a = [5,9,3]
# print(genarate(a))









# # Letter Combination of Phone Number (leetcode 17)
# class Solution(object):

#     phone = {
#         "2" : "abc",
#         "3" : "def",
#         "4" : "ghi",
#         "5" : "jkl",
#         "6" : "mno",
#         "7" : "pqrs",
#         "8" : "tuv",
#         "9" : "wxyz"
#     }

#     def combination(self, digits):
#         result = []
#         def solve(ind,subset):
            
#             if ind >= len(digits):
#                 result.append("".join(subset))
#                 return
            
#             for ch in self.phone[digits[ind]]:
#                 subset.append(ch)
#                 solve(ind+1, subset)
#                 subset.pop()


#         solve(0,[])
#         return result
# o = Solution()
# print(o.combination("9"))