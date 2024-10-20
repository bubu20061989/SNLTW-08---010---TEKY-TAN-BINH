diemToan = float(input("Nhập điểm toán: "))
diemVan = float(input("Nhập điểm văn: "))
diemTiengA = float(input("Nhập điểm tiếng anh: "))
diemTrungBinh = (diemToan + diemVan + diemTiengA)/3
if diemTrungBinh < 5:
    print("Học sinh xếp loại yếu")
elif diemTrungBinh >= 5 and diemTrungBinh < 6.5:
    print("Học sinh xếp loại trung bình")
elif diemTrungBinh >= 6.5 and diemTrungBinh <= 8:
    print("Học sinh xếp loại khá")
elif diemTrungBinh >= 8.5:
    print("Học sinh xếp loại giỏi")