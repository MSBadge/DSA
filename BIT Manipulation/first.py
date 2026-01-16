# # decimal to binary conversion
# def binary_conversion(num:int)->str:
#     result = ""
#     while num > 0:
#         if num % 2 == 1:
#             result+="1"
#         else:
#             result+="0"
#         num = num // 2
#     result = result[::-1]
#     return result

# print(binary_conversion(9))







# # binary to decimal
# def binary_to_decimal(num:str)->int:
#     decimal = 0
#     power = 0
#     index = len(num)-1
    
#     while index >= 0:
#         total = int(num[index]) * (2**power)
#         decimal += total
#         index-=1
#         power+=1
#     return decimal

# print(binary_to_decimal("1001"))








