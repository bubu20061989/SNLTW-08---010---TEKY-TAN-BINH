diemToan = float(input("Nhập điểm toán: "))
while diemToan < 0 or diemToan > 10:
    diemToan = float(input("Nhập điểm toán: "))
diemVan = float(input("Nhập điểm văn: "))
while diemVan < 0 or diemVan > 10:
    diemVan = float(input("Nhập điểm văn: "))
diemTiengA = float(input("Nhập điểm tiếng anh: "))-1
while diemTiengA < 0 or diemTiengA > 10:
    diemTiengA = float(input("Nhập điểm tiếng anh: "))
diemTrungBinh =(diemToan + diemVan + diemTiengA)/3
print("Điểm trung bình=",diemTrungBinh)