# Cho 2 số a, b bất kỳ. Hãy in ra màn hình:
# a.    a cộng b
# b.    a trừ b
# c.    a nhân b
# d.    a chia lấy nguyên b
# e.    a mũ b
# f.     a chia dư b
# g.    so sánh a và b (lớn hơn, nhỏ hơn hay bằng)
# h.    a AND b
# i.     a OR b
# j.     a XOR b
# k.   NOT a == b
# l.    a dịch phải 1 đơn vị
# m.  a dịch trái 1 đơn vị
a=float(input())
b=float(input())
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a//b=",a//b)
print("a**b=",a**b)
print("a%b=",a%b)
if a>b:
    print("a>b",a>b)
elif a==b:
    print("a=b",a==b)
else:
    print("a<b",a<b)
print(a,"and",b)

