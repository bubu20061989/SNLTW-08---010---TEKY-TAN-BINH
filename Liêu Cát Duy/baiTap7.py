nhietDo=float(input('Hãy nhập nhiệt độ:'))
if nhietDo>35:
    print('Thời tiết nóng bức')
    print('Nên ở trong nhà và sử dụng điều hòa.')
elif 30 <= nhietDo <= 35:
    print('Thời tiết nóng')
    print('Uống đủ nước và tránh ra ngoài vào buổi trưa.')
elif 25 <= nhietDo < 30:
    print('Thời tiết ấm')
    print('Có thể ra ngoài chơi thể thao hoặc dạo bộ.')
elif 20 <= nhietDo < 25:
    print('Thời tiết mát mẻ')
    print('Đi dã ngoại hoặc tham gia các hoạt động ngoài trời.')
elif 10 <= nhietDo < 20:
    print('Thời tiết lạnh')
    print(' Mặc ấm khi ra ngoài.')
elif nhietDo > 10:
    print('Thời tiết rất lạnh')
    print('Hạn chế ra ngoài, mặc thật ấm và có thể uống nước ấm.')