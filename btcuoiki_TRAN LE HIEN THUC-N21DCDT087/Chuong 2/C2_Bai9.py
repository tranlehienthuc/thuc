def TrungCot(matrix):
    n = len(matrix)
    for j in range(n - 1):
        for k in range(j + 1, n):
            if all(matrix[i][j] == matrix[i][k] for i in range(n)):
                return True
    return False
mang = [
    [1, 2, 1],
    [4, 2, 4],
    [7, 8, 7]
]
if TrungCot(mang):
    print("Ma trận có ít nhất hai cột giống nhau.")
else:
    print("Ma trận không có ít nhất hai cột giống nhau.")