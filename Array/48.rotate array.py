import numpy as np
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    https://leetcode-cn.com/problems/rotate-image/
    """
    # Solution 1： 原地旋转
    N = len(matrix)
    for row in range(N // 2):
        # 要全部遍历该行所有元素
        for col in range(N):
            matrix[row][col],matrix[N -1-row][col] = matrix[N -1-row][col],matrix[row][col]

    for row in range(N):
        # 沿对角线交换只用遍历到row
        for col in range(row):
            # 沿对角线交换
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    return matrix

    # Solution 2: 引入另一个数组
    # N = len(matrix)
    # mat = [[0]*N for _ in range(N)]
    # print(mat)
    # for i in range(N):
    #     for j in range(N):
    #         mat[j][N-1-i] = matrix[i][j] # 倒数第i个元素索引： N-1-i
    # # 不能写成 matrix = matrix_new
    # matrix[:] = mat
    # return matrix

    # Solution 3: 原地旋转
    # N = len(matrix)
    # for row in range(N//2):
    #     if N % 2 == 0:
    #         col_end_itr = N/2
    #     else:
    #         col_end_itr = (N+1)//2 # // 返回整数， / 返回小数 2.0
    #
    #     for col in range(col_end_itr):
    #         temp = matrix[row][col]
    #         matrix[row][col] = matrix[N-col-1][row]
    #         matrix[N-col-1][row] = matrix[N-row-1][N-col-1]
    #         matrix[N - row - 1][N - col - 1] = matrix[col][N-row-1]
    #         matrix[col][N - row - 1] = temp
    # return matrix



matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))
