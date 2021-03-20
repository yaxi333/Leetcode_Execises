def generate(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]

    ls = [[1], [1, 1]]
    if numRows > 2:
        for i in range(2, numRows):
            intermedia = []
            intermedia.append(1)
            for j in range(1, i):
                intermedia.append(ls[i-1][j-1]+ls[i-1][j])
            intermedia.append(1)
            ls.append(intermedia)
    return ls



print(generate(numRows=5))




