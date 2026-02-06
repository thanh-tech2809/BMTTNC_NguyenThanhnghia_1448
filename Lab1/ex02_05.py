so_h_lam = float(input("Nhập số đã làm ở đây:"))
luong_theo_h = float(input("Nhập lương theo h của bạn:"))
h_tieu_chuan = 44 #h làm trong 1 tuần
h_vuot_chuan = max(0, so_h_lam - h_tieu_chuan)

linh_luong = h_tieu_chuan * luong_theo_h + h_vuot_chuan * luong_theo_h * 1.5

print("Số tiền bạn xứng đáng nhận được:", linh_luong,":))")