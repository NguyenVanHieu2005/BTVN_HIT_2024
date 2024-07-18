#Bài 1: Tính tổng các chữ số trong một số nguyên dương
# a, Viết một chương trình yêu cầu người dùng nhập một số nguyên dương.
# Tính và in ra tổng các chữ số của số đó. Ví dụ: Đối với số 12345, tổng các chữ số là 1 + 2 + 3 + 4 + 5 = 15
n=int(input())
tongchuso=0
while n>0:
    p=n%10
    tongchuso+=p
    n//=10
print("tổng các chữ số là ", tongchuso)

# b,Tính tổng các ước số của một số nguyên dương:
# Viết một chương trình yêu cầu người dùng nhập một số nguyên dương n. 
# Tính và in ra tổng của tất cả các ước số của n. Ước số của một số là các số mà chia hết cho số đó mà không dư. 
# Ví dụ: Ước số của 6 là 1, 2, 3, và 6.
j=int(input())
tonguoc=0
for i in range(1,j+1,1):
    if j%i==0:
        tonguoc+=i
print("tổng các ước là ", tonguoc)

# c,Kiểm tra tam giác:
# Viết chương trình yêu cầu người dùng nhập vào 3 số nguyên dương. 
# Kiểm tra xem 3 số đó có tạo thành tam giác hay không? 
# Nếu có thì đó là tam giác gì?(Cân, đều, vuông, nhọn, tù)
a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    print("3 cạnh a, b, c tạo thành tam giác")
else:
    print("3 cạnh không tạo thành tam giác")

if a==b and b==c:
    print("tam giác là tam giác đều")
elif a==b or a==c or b==c:
    print("tam giác là tam giác cân")
elif (a**2)+(b**2)==(c**2) or (b**2)+(c**2)==(a**2) or (a**2)+(c**2)==(b**2):
    print("tam giác là tam giác vuông")
elif (a**2)+(b**2)>c**2 or (a**2)+(c**2)>b**2 or (c**2)+(b**2)>c**2:
    print("tam giác là tam giác nhọn")
else:
    print("tam giác là tam giác tù")


    

