diemToan=float(input('Hãy nhập điểm môn toán'))
diemVan=float(input('Hãy nhập điểm môn văn'))
diemTiengAnh=float(input('Hãy nhập điểm môn tiếng anh'))

if diemToan > 10 or diemToan<0:
    print('Bạn đã nhập sai')
if diemVan > 10 or diemVan<0:
    print('Bạn đã nhập sai')
if diemTiengAnh > 10 or diemToiengAnh<0:
    print('Bạn đã nhập sai')

diemTrungBinh=(diemToan+diemVan+diemTiengAnh)/3
print(diemTrungBinh)
if diemTrungBinh < 5 :
    print("Yếu")
elif diemTrungBinh > 5 and diemTrungBinh < 6.5:
    print("Trung bình")
elif diemTrungBinh > 6.5 and diemTrungBinh < 8:
    print("khá")
elif diemTrungBinh >= 8:
    print("Giỏi")
