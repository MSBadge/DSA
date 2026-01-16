# # Print all subset 
# def all_subset(nums):
#     result = []

#     def backtrack(index,subset):
#         if index >= len(nums):
#             result.append(subset.copy())
#             return
#         subset.append(nums[index])
#         backtrack(index + 1,subset)
#         subset.pop()
#         backtrack(index + 1,subset)
#     backtrack(0,[])
#     return result

# nums = [5,9,7]
# print(all_subset(nums))








# # genarate sequence with sum k
# def genrate(nums,target):
#     result = []

#     def badktrack(index,total,subset):
        
#         if total == target:
#             result.append(subset.copy())
#             return
        
#         if index >= len(nums) or total > target:
#             return
        
#         subset.append(nums[index])
#         summ = total + nums[index]

#         badktrack(index + 1,summ,subset)
#         e = subset.pop()
#         summ -= e
#         badktrack(index+1,summ ,subset)

#     badktrack(0,0,[])
#     return result

# nums = [5,9,4]
# target = 9
# print(genrate(nums,target))






# # Check if there exists a subsequence with sum K
# def genarate(nums,k):
#     result = []

#     def backtrack(index,total,subset):
#         if index >= len(nums) or total > k:
#             return False

#         if total == k:
#             result.append(subset.copy())
#             return True
        
#         subset.append(nums[index])
#         summ = total + nums[index]

#         if backtrack(index+1,summ,subset):
#             return True
        
#         subset.pop()

#         return backtrack(index+1,total,subset)
    
#     return backtrack(0,0,[])
    

# a = [5,9,4]
# print(genarate(a,9))








# # Count all Subsequences with sum = K
# def count(num,k):
#     def backtrack(index, total):

#         if total == k:
#             return 1
        
#         if index >= len(num) or total > k:
#             return 0
        
#         summ = total + num[index]
        
#         pick = backtrack(index+1, summ)
#         summ = total
#         not_pick = backtrack(index+1, summ)
#         return pick + not_pick

#     return backtrack(0,0)

# a = [5,9,4]
# k = 9
# print(count(a,k))





