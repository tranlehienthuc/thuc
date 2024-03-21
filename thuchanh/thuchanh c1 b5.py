def sum_of_divisors(n):
    sum_divisors = 1  # Số 1 luôn là ước số của mọi số nguyên dương
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors
def classify_number(n):
    divisor_sum = sum_of_divisors(n)
    if divisor_sum < n: #nếu nhỏ hơn n sẽ là deficient
        return "deficient"
    elif divisor_sum == n: #nếu bằng n sẽ là perfect
        return "perfect"
    else: #ngược lại là abundant
        return "abundant"
def Number(x, y):
    for i in range(x, y + 1):
        print("Số", i, "là", classify_number(i))

# Ví dụ 
x = int(input("nhap x: "))
y = int(input("nhap y: "))
Number(x, y)
