print("SD HÀM STRINGS")
s = input("Nhập chuỗi s:\n")
s_sub = input("Nhập chuỗi con s_sub:\n")
s_find = input("Nhập chuỗi tìm s_find:\n")
s_replace = input("Nhập chuỗi thay thế s_replace:\n")
xoa = s.strip()
ktr = xoa.replace(s_find, s_replace)
print("Chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối chuỗi:", xoa)
print("Số lần s_sub xuất hiện trong s:", s.count(s_sub))
print("Chuỗi s sau khi tìm kiếm và thay thế:", ktr.capitalize())