# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 -> 3200 . Các số thu được in thành chuỗi trên 1 dòng, cách nhau bằng dấu phẩy

j = []
for i in range (2000, 3200):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print(','.join(j))