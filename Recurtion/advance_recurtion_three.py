# # N-Queens (leetcode 51)
# def genarate_queen(n):
#     ans = []
#     board = ["." * n for _ in range(n)]
#     left_row = [0] * n
#     upperDiagonal = [0] * (2 * n - 1)
#     lowerDiagonal = [0] * (2 * n - 1)

#     def solve( col, board, ans, left_row, upperDiagonal, lowerDiagonal):
#         if col == n :
#             ans.append(board[:])
        
#         for row in range(n):
#             if (
#                 left_row[row] == 0
#                 and lowerDiagonal[row + col] == 0
#                 and upperDiagonal[n -1 + col - row] == 0
#             ):
#                 board[row] = board[row][:col] + "Q" + board[row][col + 1:]
#                 left_row[row] = 1
#                 lowerDiagonal[row + col] = 1
#                 upperDiagonal[n - 1 + col - row] = 1

#                 solve(col + 1, board, ans, left_row, upperDiagonal, lowerDiagonal)

#                 board[row] = board[row][:col] + "." + board[row][col + 1:]
#                 left_row[row] = 0
#                 lowerDiagonal[row + col] = 0
#                 upperDiagonal[n -1 + col - row] = 0
#     solve(0, board, ans, left_row, upperDiagonal, lowerDiagonal)
#     return ans

# print(genarate_queen(4))











# # Rat in Maze problem 1
# def findPathHelper(
#     i: int, j: int, a: List[List[int]], n: int, 
#     ans: List[str], move: str, vis: List[List[int]]
# ):
#     # Base case: reached destination
#     if i == n - 1 and j == n - 1:
#         ans.append(move)
#         return

#     # Try going downward (i+1, j)
#     if i + 1 < n and not vis[i + 1][j] and a[i + 1][j] == 1:
#         vis[i][j] = 1  # Mark current cell as visited
#         findPathHelper(i + 1, j, a, n, ans, move + "D", vis)
#         vis[i][j] = 0  # Backtrack: unmark current cell

#     # Try going left (i, j-1)
#     if j - 1 >= 0 and not vis[i][j - 1] and a[i][j - 1] == 1:
#         vis[i][j] = 1
#         findPathHelper(i, j - 1, a, n, ans, move + "L", vis)
#         vis[i][j] = 0

#     # Try going right (i, j+1)
#     if j + 1 < n and not vis[i][j + 1] and a[i][j + 1] == 1:
#         vis[i][j] = 1
#         findPathHelper(i, j + 1, a, n, ans, move + "R", vis)
#         vis[i][j] = 0

#     # Try going upward (i-1, j)
#     if i - 1 >= 0 and not vis[i - 1][j] and a[i - 1][j] == 1:
#         vis[i][j] = 1
#         findPathHelper(i - 1, j, a, n, ans, move + "U", vis)
#         vis[i][j] = 0

# def ratMaze(matrix: List[List[int]]) -> List[str]:
#     n = len(matrix)
#     ans = []
#     vis = [[0 for _ in range(n)] for _ in range(n)]  # Visited array
    
#     # Only start if source cell is open
#     if matrix[0][0] == 1:
#         findPathHelper(0, 0, matrix, n, ans, "", vis)
#     return ans