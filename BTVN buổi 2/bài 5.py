
n = int(input("Nhập số n: "))
for i in range(1, n + 1):
    a = i
    b = 0  
    while a > 0:
        c = a % 10
        b += c ** 3
        a //= 10
    if b == i:
        print(i)
