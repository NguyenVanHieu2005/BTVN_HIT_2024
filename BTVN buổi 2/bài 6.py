n = int(input("Nhập số nguyên n: "))
for i in range(1,n+1):
    tong=0
    for j in range(1,n+1):
        if i%j==0:
           tong+=j

    if tong==i and i!=1:
        print(i," là số hoàn hảo")
