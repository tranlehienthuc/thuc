# Phương thức tính GCD sử dụng đệ qui
def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)
# Ví dụ
m = int(input("nhap m: "))
n = int(input("nhap n: "))
gcd_recursive_result = gcd_recursive(m, n)
print("Ước số chung lớn nhất của", m, "và", n, "là:", gcd_recursive_result)