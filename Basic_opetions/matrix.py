# # 2d matrix
# a = [[5,0],[2,4]]
# row = len(a)
# col = len(a[0])

# for i in range(row):
#     for j in range(col):
#         print(a[i][j], end=" ")
#     print()




# # Print upper triangel
# a = [[5,7,3],[2,4,9],[8,1,6]]
# row = len(a)
# col = len(a[0])

# for i in range(row):
#     for j in range(col):
#         if j >= i:
#             print(a[i][j], end=" ")
#         else:
#             print("*", end=" ")       
#     print()




# # Print lower triangel
# a = [[5,7,3],[2,4,9],[8,1,6]]
# row = len(a)
# col = len(a[0])

# for i in range(row):
#     for j in range(col):
#         if j <= i:
#             print(a[i][j], end=" ")
#         else:
#             print("*", end=" ")   
#     print()




# # Print diagonal triangel
# a = [[5,7,3],[2,4,9],[8,1,6]]
# row = len(a)
# col = len(a[0])

# for i in range(row):
#     for j in range(col):
#         if j != i:
#             print(a[i][j], end=" ")
#         else:
#             print("*", end=" ")   
#     print()




# Print opposite diagonal triangel







# # transfose of a metrix
# matrix = [[5,9,1],[2,3,7]]
# row = len(matrix)
# colume = len(matrix[0])
# result = [[0]*row for _ in range(colume)]
# for i in range(row):
#     for j in range(colume):
#         result[j][i]= matrix[i][j]
# print(result)





# Set matrix zeros (brute solution)
