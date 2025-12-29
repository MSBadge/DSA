# # Two Sum (brute solution)
# def add(num,target):
#     n = len(num)
#     for i in range(n):
#         for j in range(i+1,n):
#             if num[i]+num[j]== target:
#                 return [i,j]

# a = [2,7,11,15]
# target = 22
# print(add(a,target))





# # Two Sum (optimal solution)
# def add(nums,target):
#     n = len(nums)
#     dic = {}
#     i = 0
#     while i < n:
#         r = target - nums[i]
#         if r in dic:
#             return [dic[r],i]
#         else:
#             dic[nums[i]]=i
#         i+=1
# a = [2,7,11,15]
# target = 22
# print(add(a,target))


# # Two Sum (optimal solution)
# def add(nums,target):
#     n = len(nums)
#     dic = {}
#     for i in range(n):
#         r = target - nums[i]
#         if r in dic:
#             return [dic[r],i]
#         dic[nums[i]]=i
# a = [2,7,11,15]
# target = 9
# print(add(a,target))





# # Kadane's Algorithm, maximum subarray sum (brute solution)
# def subarray(num):
#     n = len(num)
#     maxi = float("-inf")
#     for i in range(n):
#         total = 0
#         for j in range(i,n):
#             total = total + num[j]
#             if maxi < total:
#                 maxi =  total
#             else:
#                 maxi = maxi
#     return maxi
# a = [-1,2,-3,4]
# print(subarray(a))





# # Kadane's Algorithm, maximum subarray sum (optimal solution)
# def subarray(num):
#     n = len(num)
#     maxi = float("-inf")
#     total = 0
#     for i in range(n):
#         total = total+num[i]
#         if total <= 0:
#             total = 0
#         maxi = max(maxi,total)

#     return maxi

# a = [-1,2,-3,4,5]
# print(subarray(a))






# # Stock buy and sell (brute force solution)
# def stock(price):
#     n = len(price)
#     maxi = 0
#     for i in range(n):
#         for j in range(i+1,n):
#             t = price[j] - price[i]
#             if maxi < t:
#                 maxi = t
#     if maxi <= 0:
#         return 0

#     return maxi
# prices = [7,6,9,2,0]
# print(stock(prices))






# # Stock buy and sell (optimal solution)
# def stock(prices):
#     n = len(prices)
#     min_price = float("inf")
#     maxi = 0
#     for i in range(n):
#         min_price = min(min_price,prices[i])
#         profit = prices[i]-min_price
#         maxi = max(maxi,profit)
#     return maxi
# prices = [7,1,5,3,6,4]
# print(stock(prices))






# # Stock buy and sell (optimal solution)
# def stock(prices):
#     n = len(prices)
#     min_price = float("inf")
#     maxi = 0
#     for i in range(n):
#         if prices[i]<min_price:
#             min_price=prices[i]
#         profit = prices[i]-min_price
#         if profit > maxi:
#             maxi = profit
#     return maxi
# prices = [7,1,5,3,6,4]
# print(stock(prices))






# # Rearrange array elements by sign (brute solution)
# def rearrange(nums):
#     n = len(nums)
#     pos = []
#     neg = []
#     for i in range(n):
#         if nums[i] >= 0:
#             pos.append(nums[i])
#         else:
#             neg.append(nums[i])
#     for j in range(len(pos)):
#             nums[j*2] = pos[j]
#             nums[j*2+1] = neg[j]
#     return nums
# a = [5,10,-3,-6,-10,6,4,-7]
# print(rearrange(a))





# # Rearrange array elements by sign (optimal solution)
# def rearrange(nums):
#     l = len(nums)
#     result = [0]*l
#     p = 0
#     n = 1
#     for i in range(l):
#         if nums[i]>=0:
#             result[p] = nums[i]
#             p+=2
#         else:
#             result[n] = nums[i]
#             n+=2    
#     return result
# a = [5,10,-3,-6,-10,6,4,-7]
# print(rearrange(a))






# # longest consecutive sequence (brute solution)
# def consecutive(nums):
#     n = len(nums)
#     maxi = 0
#     for i in range(n):
#         count = 1
#         no = nums[i]
#         while no+1 in nums:
#             count+=1
#             no+=1
#         if count > maxi:
#             maxi = count
#     return maxi
# a = [1,1,1,2,3,65,0]
# print(consecutive(a))





# # longest consecutive sequence (better solution)
# def consecutive(nums):
#     nums.sort()
#     n = len(nums)
#     count = 0
#     last_smaller = float("-inf")
#     longest = 0
#     for i in range(n):
#         num = nums[i]
#         if num-1==last_smaller:
#             count+=1
#             last_smaller=num
#         elif num != last_smaller:
#             count=1
#             last_smaller=num
#         longest =  max(longest,count)
#     return longest

# a = [1,1,1,5,99,2,101,3,98,100]
# print(consecutive(a))








# # longest consecutive sequence (optimal solution)
# def consecutive(nums):
#     s = set(nums)
#     longest = 0
#     for i in s:
#         if i-1 not in s:
#             x = i
#             count =1
#             while x+1 in s:
#                 count+=1
#                 x+=1
#             longest = max(longest, count)
#     return longest

# a = [1,1,1,5,99,2,101,3,98,100]
# print(consecutive(a))

