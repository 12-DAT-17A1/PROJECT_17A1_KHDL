tp = eval(input("Tuple: "))
counts = len(tp)
select1 = int(input(f"Nhập số từ 0 đến {counts-1}: "))
select2 = int(input(f"Nhập số từ -1 đến {1-counts}: "))
select3 = input("Nhập chuỗi cần tìm: ")
find = tp.count(select3)
print(f"Tuple [{select1}] =", tp[select1])
print(f"Tuple [{select2}] =", tp[select2])
print(f"{select3} xuất hiện {find}")
