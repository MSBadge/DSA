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





# # Set matrix zeros (brute solution)
# matrix = [[1,2,3,4],[5,0,7,8],[7,4,0,1],[8,5,2,3]]
# row = len(matrix)
# col = len(matrix[0]) 

# for i in range(row):
#     for j in range(col):
#         print(matrix[i][j], end=" ")
#     print()
# print()

# def mark(matrix,row,col):
#     for i in range(row):
#         if matrix[i][col] != 0:
#             matrix[i][col] = float("inf")

#     for j in range(col):
#         if matrix[row][j]!=0:
#             matrix[row][j] = float("inf")
#     return matrix

# def setZero(matrix):
#     row = len(matrix)
#     col = len(matrix[0])
#     for i in range(row):
#         for j in range(col):
#             if matrix[i][j]==0:
#                 mark(matrix,i,j)
#     for i in range(row):
#         for j in range(col):
#             if matrix[i][j] == float("inf"):
#                 matrix[i][j] = 0
#             print(matrix[i][j], end=" ")
#         print()
#     return f"{matrix[i][j]}{'\n'}"
# print(setZero(matrix))







# # Set matrix zeros (optimal solution)
# def zeros(mat):
#     r = len(mat)
#     c = len(mat[0])
#     r_track = [0 for _ in range(r)]
#     c_track = [0 for _ in range(c)]

#     for i in range(r):
#         for j in range(c):
#             if mat[i][j] == 0:
#                 r_track[i] = -1
#                 c_track[j] = -1

#     for i in range(r):
#         for j in range(c):
#             if r_track[i] == -1 or c_track[j] == -1:
#                 mat[i][j] = 0

#     for i in range(r):
#         for j in range(c):
#             print(mat[i][j], end=" ")
#         print()
# matrix = [[1,2,3,4],[5,0,7,8],[7,4,0,1],[8,5,2,3]]
# zeros(matrix)







# # Rotate matrix by 90 Degree [In Place] (brute solution)
# matrix = [[1,2,3,4],[5,0,7,8],[7,4,0,1],[8,5,2,3]]

# def degree(mat):
#     n = len(mat)
#     result = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             result[j][(n-1)-i] = mat[i][j]

#     for i in range(n):
#         for j in range(n):
#             print(mat[i][j],end=" ")
#         print()
#     print()

#     for i in range(n):
#         for j in range(n):
#             print(result[i][j],end=" ")
#         print()

# degree(matrix)







# # Rotate matrix by 90 Degree [In Place] (optimal solution)
# matrix = [[1,2,3,4],[5,0,7,8],[7,4,0,1],[8,5,2,3]]
# n = len(matrix)
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=" ")
#     print()
# print()

# def rotate(mat):
#     n = len(mat)
#     for i in range(n):
#         for j in range(i+1,n):
#             mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

#     for i in range(n):
#         mat[i].reverse()

#     for i in range(n):
#         for j in range(n):
#             print(mat[i][j], end=" ")
#         print()
    
# rotate(matrix)









# Spiral matrix (brute solution)
def spiral(mat):

    result = []

    row = len(mat)
    col = len(mat[0])
    top, left = 0,0
    bottom, right = row-1, col-1
    while top <= bottom and left <= right:
        # left to right 
        for i in range(left, right+1):
            result.append(mat[top][i])
        top+=1

        # top to bottom
        for i in range(top, bottom+1):
            result.append(mat[i][right])
        right-=1

        # right to left
        if top <= bottom:
            for i in range(right, left-1,-1):
                result.append(mat[bottom][i])
            bottom-=1

        # bottom to top
        if left <= right:
            for i in range(bottom, top-1,-1):
                result.append(mat[i][left])
            left+=1

    return result

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiral(matrix))











def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Make sure we still have rows and columns to traverse
        if top <= bottom:
            # Traverse from right to left along the bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # Traverse from bottom to top along the left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiralOrder(matrix))


