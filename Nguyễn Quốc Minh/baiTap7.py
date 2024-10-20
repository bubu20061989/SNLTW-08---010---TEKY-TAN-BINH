nhietDo=float(input('Hãy nhập nhiệt độ của một ngày '))
if nhietDo > 35:
    print('Thời tiết nóng bức ')
elif nhietDo >30 and nhietDo <35:
    print('Thời tiết nóng ')
elif nhietDo >25 and nhietDo <30:
    print('Thời tiết ấm ')
elif nhietDo >20 and nhietDo <25:
    print('Thời tiết mát mẻ ')
elif nhietDo >10 and nhietDo <20:
    print('Thời tiết lạnh ')
elif nhietDo <10:
    print('Thời tiết rất lạnh ')

if nhietDo >= 'nóng bức ':
    print('Khuyên người dùng nên ở trong nhà và sử dụng điều hòa')
elif nhietDo >= 'nóng ':
    print('Khuyên người dùng uống đủ nước và tránh ra ngoài vào buổi trưa')
elif nhietDo >= 'ấm ':
    print('Khuyên người dùng có thể ra ngoài chơi thể thao hoặc dạo bộ')
elif nhietDo >= 'mát mẻ ':
    print('Khuyên người dùng đi dã ngoại hoặc tham gia các hoạt động ngoài trời')
elif nhietDo >= 'lạnh ':
    print('Khuyên người dùng mặc ấm khi ra ngoài')
elif nhietDo >= 'rất lạnh ':
    print('Khuyên người dùng hạn chế ra ngoài, mặc thật ấm và có thể uống nước ấm')

#qm