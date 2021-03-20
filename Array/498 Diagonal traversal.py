

def findDiagonalOrder(matrix):

    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    # Solution 1(有bug)

    # results = []
    # l = len(matrix)
    # w = len(matrix[0])
    #
    # # 先按照第一行遍历:
    # for iter_i in range(w):
    #     j = 0
    #     # 1. i 的值会变化，遇到两重循环且循环条件变量重复时，要注意！
    #     i = iter_i
    #     # 初始化每一个对角线存放的暂时列表，每一次开始新的遍历前清空
    #     ls = []
    #     # 2. 设置idx索引范围在矩阵范围内的方法：
    #     # 注意： idx 最后一行/列 = 长度/宽度 - 1
    #     while j <= l - 1 and j >= 0 and i <= w - 1 and i >= 0:
    #         #
    #         ls.append(matrix[j][i])
    #         # 从上往下遍历 下一个坐标为（j+1，i-1）
    #         j += 1
    #         i -= 1
    #     # 如果遍历的这一行Idx为偶数，则反转ls
    #     if iter_i % 2 == 0:
    #         # 3. 用 extend 直接增加列表中的元素 & append 增加列表
    #         results.extend(ls[::-1])
    #     else:
    #         # 4. python3 != 符号已经废弃，只能用 ==
    #         results.extend(ls)
    #
    #
    # # 按照最后一列遍历：
    # # 右上角的元素已经遍历过了在行的时候
    # for iter_j in range(1, l):
    #     # 从最后一列开始，i初始值为w-1
    #     i = w - 1
    #     j = iter_j
    #     ls = []
    #     while j <= l - 1 and j >= 0 and i <= w - 1 and i >= 0:
    #         ls.append(matrix[j][i])
    #         j += 1
    #         i -= 1
    #     if w>=l:
    #         if iter_j % 2 == 0:
    #             results.extend(ls[::-1])
    #         else:
    #             results.extend(ls)
    #     else:
    #         if iter_j % 2 == 0:
    #             results.extend(ls)
    #         else:
    #             results.extend(ls[::-1])
    #
    #
    # return results

    # Solution 2
    # # We need to figure out the "head" of this diagonal
    #             # The elements in the first row and the last column
    #             # are the respective heads.
    #


    # Check for empty matrices
    if not matrix or not matrix[0]:
        return []

    # Variables to track the size of the matrix N*M
    N, M = len(matrix), len(matrix[0])

    # Initialize the two arrays as explained in the algorithm
    result, intermediate = [], []

    # We have to go over all the elements in the first
    # row and the last column to cover all possible diagonals
    for d in range(N + M - 1):

        # Clear the intermediate array everytime we start
        # to process another diagonal
        intermediate.clear()

        # We need to figure out the "head" of this diagonal
        # The elements in the first row and the last column
        # are the respective heads.
        r = 0 if d <= M-1 else d - M + 1
        c = d if d <= M-1 else M - 1




        # Iterate until one of the indices goes out of scope
        # Take note of the index math to go down the diagonal
        while r < N and c > -1:
            intermediate.append(matrix[r][c])
            r += 1
            c -= 1

        # Reverse even numbered diagonals. The
        # article says we have to reverse odd
        # numbered articles but here, the numbering
        # is starting from 0 :P
        if d % 2 == 0:
            result.extend(intermediate[::-1])
        else:
            result.extend(intermediate)
    return result




matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Ri:", [1,2,5,9,6,3,4,7,10,11,8,12])
print("My:", findDiagonalOrder(matrix))