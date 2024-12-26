# Viết 1 ct tính giai thừa của 1 số cho trước . Kết quả được in ra thành chuỗi trên 1 dòng phân tách bởi dấu phẩy . Ví dụ , số cho là 8 thì kết quả phải là 40320
"""     0! = 1 (theo quy ước)
    x! = x * (x - 1) * (x - 2) * ... * 3 * 2 * 1 """

x=int(input("Nhập số cần tính giai thừa : "))
def fact(x):
    if x<0:
        return print("Nhập giá trị phải lớn hơn hoặc 0")
    if x==0:
        return 1
    return x * fact(x-1)
print(fact(x))