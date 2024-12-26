# Vớ số nguyên n nhất định, hãy viết ct để tạo 1 dictionary chứa (i, i*i) nh7 là 1 số nguyên từ 1 đến n sau đó in ra dictionary này . 
# Vd : n = 8 thì đầ ra sẽ là : {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:42, 8:64}

n = int(input("Nhập vào 1 số nguyên dương : "))
d = dict()

for i in range (1,n+1):
    d[i] = i*i

print(d)    