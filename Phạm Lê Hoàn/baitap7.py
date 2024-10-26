nhietDo = float(input("Nhập nhiệt độ của một ngày"))
if nhietDo > 35:
    print("Thời tiết nóng bức")
elif nhietDo > 30 and nhietDo < 35:
    print("Thời tiết nóng")
elif nhietDo > 25 and nhietDo < 30:
    print("Thời tiết ấm")
elif nhietDo > 20 and nhietDo < 25:
    print("Thời tiết mát mẻ") 
elif nhietDo > 15 and nhietDo < 20:
    print("Thời tiết lạnh")
elif nhietDo < 10:
    print("Thời tiết rất lạnh")
if nhietDo > 35:
     print('Khuyên người dùng nên ở trong nhà và sử dụng điều hòa.')
elif nhietDo > 30 and nhietDo < 35:
     print('Khuyên người dùng uống đủ nước và tránh ra ngoài vào buổi trưa.')
elif nhietDo > 25 and nhietDo < 30:
     print("Khuyên người dùng có thể ra ngoài chơi thể thao hoặc dạo bộ.")
elif nhietDo > 20 and nhietDo < 25:
     print('Khuyên người dùng đi dã ngoại hoặc tham gia các hoạt động ngoài trời.')
elif nhietDo > 15 and nhietDo < 20:
     print("Khuyên người dùng mặc ấm khi ra ngoài.")
elif nhietDo < 10:
     print('Khuyên người dùng hạn chế ra ngoài, mặc thật ấm và có thể uống nước ấm.')