# https://leetcode-cn.com/problems/zero-matrix-lcci/

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # Solution 1 复杂度更高，因为存在矩阵转置2次；空间复杂度也高，因为
    # 设置了新的矩阵，并且用两个新的list 存放为 0 的下标
    # rown = len(matrix)
    # coln = len(matrix[0])
    # col_zero_ls = []
    # row_zero_ls = []
    # matrix_new = [[0]*rown for _ in range(coln)]
    #
    # # save col which is o
    # for row in range(rown):
    #     for col in range(coln):
    #         if matrix[row][col] == 0:
    #             col_zero_ls.append(col)
    #             row_zero_ls.append(row)
    #
    # #行置零
    # for i in row_zero_ls:
    #     matrix[i][:] = [0]*coln
    # print(matrix)
    # # 转置行置零后的矩阵, 不是对称矩阵不能这样转置
    # for row in range(rown):
    #     # 沿对角线交换只用遍历到row
    #     for col in range(coln):
    #         # 沿对角线交换
    #         matrix_new[col][row] = matrix[row][col]
    # print(matrix_new)
    #
    # # 列置零：现在的行是之前的列，所以重复之前对行置零的做法即可，但只对有0的行
    # # 否则新置零的行也会被检测为有0的列，变成全零matrix
    # for i in col_zero_ls:
    #     matrix_new[i][:] = [0]*rown
    #
    # # 转置行置零后的矩阵, 不是对称矩阵不能这样转置
    # for row in range(rown):
    #     # 沿对角线交换只用遍历到row
    #     for col in range(coln):
    #         # 沿对角线交换
    #         matrix[row][col] = matrix_new[col][row]
    # print(matrix)
    #
    # return matrix


    # Solution 2
    '''
        刚开始看到这道题，首先想到的就是遍历寻找0的位置，并且在循环结束之前不能改变矩阵，否则会导致矩阵全部被清零。在找到了0时，首先想到的就是使用额外的二维数组空间存储0的坐标，但画图可以发现，当某处出现零时，其所在列、所在行的所有节点都将会清零，那么我们不如把0元素的横纵坐标分别用所在列、所在行的第一个元素变成0来记录，因为迟早都会被清零。最后清零时遍历第一行和第一列，然后对其行、列赋0即可。
    
    规定：第一行的零用来清所在列的零，第一列的零用来清所在行的零。唯一特殊的位置就是a[0][0]处，因为其位于行列的交叉点，无法确定具体表示行/列清零，因此我们需要额外一个存储空间定义为int initialLine = 1，将a[0][0]规定为第0行清零，initialLine规定为第0列清零，这样就能仅使用O(1)的额外空间来完成题目。
    
    核心：就是使用两个一维的清零组合替代一个二维的清零，同时两个一维的清零的所在行列共同构成二维清零的坐标，从而用数组本身存储了0元素的信息
    
    作者：bei-zhi-hu
    链接：https://leetcode-cn.com/problems/zero-matrix-lcci/solution/cling-ju-zhen-kong-jian-fu-za-du-o1-by-b-ffkg/

    '''

    rown = len(matrix)
    coln = len(matrix[0])
    row_zero = False
    column_zero = False

    for col in range(coln):
        if matrix[0][col] == 0:
            row_zero = True
    for row in range(rown):
        if matrix[row][0] == 0:
            column_zero = True

    # save the first element of the corresponding col and row when occur 0
    for row in range(1, rown):
        for col in range(1, coln):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0
    # print(matrix)

    # 遍历第一行，列置零
    for col in range(1, coln):
        if matrix[0][col] == 0:
            for row in range(rown):
                matrix[row][col] = 0
    # print(matrix)

    # 遍历第一列，行置零
    for row in range(1, rown):
        if matrix[row][0] == 0:
            matrix[row][:] = [0]*coln
    # print(matrix)


    # 最后再对第一行第一列置零：只要第一行/列含有0， 就对应对行/列置零，要分开，否则又是全零
    if row_zero:
        matrix[0][:] = [0]*coln
    if column_zero:
        for row in range(rown):
            matrix[row][0] = 0

    return matrix








matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)
print(setZeroes(matrix))