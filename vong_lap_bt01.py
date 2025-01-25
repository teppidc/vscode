# Cho 1 số tự nhiên n (n <= 10^1000). Tính tổng các số hạng của n 
# Ví dụ : n= 123 , tổng các sống hạng của n = 1 + 2 + 3 = 6
n = int(input("Nhập số tự nhiên n : "))
s = 0
while n > 0:
    s = s + n%10 # m % 10 : số dư khi n chia cho 10
    print(s)  # check vòng lặp
    n = n//10 # là thương khi chia hết cho 10
print("Tổng các số hạng của n :",s)