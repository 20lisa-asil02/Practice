from sys import setrecursionlimit
setrecursionlimit(10**7)
def longest_increasing_path(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(row, col):
        if (row, col) in memo:
            return memo[(row, col)]

        longest = 1
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                longest = max(longest, 1 + dfs(new_row, new_col))

        memo[(row, col)] = longest
        return longest

    memo = {}
    ans = 0
    for i in range(rows):
        for j in range(cols):
            ans = max(ans, dfs(i, j))

    return ans

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(longest_increasing_path(matrix))


# 2 3
# 10 8 5
# 10 5 4

# 4

