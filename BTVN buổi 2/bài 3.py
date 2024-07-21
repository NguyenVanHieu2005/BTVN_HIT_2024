# Bài 3: Tính các tổng sau:
# S(n) = 1 - 2 + 3 - 4 + 5 + .... + (2*n + 1)
# S(n) = 1 + ½ + ⅓ + ¼ +.....+1/n
# Biện luận nghiệm của phương trình bậc 2 một ẩn
n=int(input("nhập n"))
Tong=1
for i in range(1,n+1,1):
    Tong=Tong-2*i+(2*i+1)
print("Tổng 1-2+3-4+5+...+2*n+1 là",Tong)
tong=0
for i in range(1,n+1,1):
    tong+=1/i
print("Tổng 1 + ½ + ⅓ + ¼ +.....+1/n là ", tong)
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta=b**2-4*a*c
if delta>0:
    x1=(-b+delta/2)/(2*a)
    x2=(-b-delta/2)/(2*a)
    print("phương trình có 2 nghiệm riêng biệt là ")
    print("x1= ",x1)
    print("x2= ",x2)
elif delta==0:
    x=-b/2*a
    print("phương trình có nghiệm kép là x= ",x)
else:
    print("phương trình vô nghiệm")
