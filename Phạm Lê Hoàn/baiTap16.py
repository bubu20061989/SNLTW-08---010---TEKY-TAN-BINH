#chuoi = "phamlehoan"
#print(chuoi)

#aa = "le"
#b = "hoan"
#print(b*3)
#print(len(aa))

#a = "le hoan tu"
#c = a.replace("le","6A12")
#print(c)
#d = a.find("tu")
#print(d)

#a = "pham le hoan"
# e = a.split()
# print(e)
#f = a.replace("pham"," ")
#print(f)
#b = a.lower()
#print(b)




chuoi = input("nhập vào 1 chuỗi:")
while True:
    print("MENU XỬ LÝ VĂN BẢN")
    print("1.Thay thế")
    print("2.tìm kiếm")
    print("3.Độ dài chuỗi")
    luachon = int(input("nhập lựa chọn"))
    if(luachon== 1):
        tuCu = input("nhập từ cần thay thê: ")
        tuMoi = input("nhập từ thay thế: ")
        chuoiMoi = chuoi.replace(tuCu,tuMoi)
        print("văn bản sửa xong: ",chuoiMoi)
    elif(luachon==2):
        tuMuonTimKiem=input('Từ muốn tìm kiếm: ')
        vitricuatu = chuoi.find(tuMuonTimKiem)
        print(vitricuatu)
    elif(luachon==3):
        print(len(chuoi))
    else:
        break