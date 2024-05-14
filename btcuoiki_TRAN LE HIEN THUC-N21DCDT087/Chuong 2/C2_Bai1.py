def mang_doi_xung(matrix):
    return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix[0])))
mang = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
if mang_doi_xung(mang):
    print("Ma tran doi xung.")
else:
    print("Ma tran khong doi xung.")