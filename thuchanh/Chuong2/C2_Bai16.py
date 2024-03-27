def Dao(matrix):
    n = len(matrix)
    areas = []
    for i in range(n):
        temp = [0] * n
        for j in range(i, n):
            temp = [temp[k] + matrix[j][k] for k in range(n)]
            area = (j - i + 1) * max(temp)
            areas.append(area)
    return max(areas)
matrix = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0]
]
result = Dao(matrix)
print(f"Diện tích lớn nhất của các đảo hình chữ nhật: {result}")