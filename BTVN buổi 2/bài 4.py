# Bài 4:  Dãy số Fibonacci
# Hãy viết chương trình tìm n số Fibonacci đầu tiên.
# Quy luật của dãy số Fibonacci: số tiếp theo bằng tổng của 2 số trước, 2 số đầu tiên của dãy số là 0, 1.
# Ví dụ: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
print("Nhap so n:")
n=int(input())
f0=0
f1=1
f2=1
print("n so fib dau tien la:")
print(f0,f1,f2)
for i in range(n,2,-1):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3, end=' ')
print()
