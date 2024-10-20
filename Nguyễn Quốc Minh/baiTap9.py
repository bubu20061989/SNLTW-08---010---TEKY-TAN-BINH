diemToan=float(input('Hãy nhập điểm toán '))
diemVan=float(input('Hãy nhập điểm văn '))
diemTiengAnh=float(input('Hãy nhập điểm tiếng anh'))

while diemToan < 0 or diemToan > 10:
    diemToan= float(input('Điểm toán đã nhập sai vui lòng nhập lại '))
while diemVan < 0 or diemVan > 10:
    diemVan= float(input('Điểm văn đã nhập sai vui lòng nhập lại '))
while diemTiengAnh < 0 or diemToan > 10:
    diemTiengAnh= float(input('Điểm tiếng anh đã nhập sai vui lòng nhập lại '))
    
print('Điểm trung bình của cả ba môn là',(diemToan+diemVan+diemTiengAnh)/3)
