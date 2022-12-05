from himn import *

def modau():
    global m
    print('__________________HELLO WORLDCUP___________________')
    print("__1. Tra cứu kết quả thi đấu ")
    print("__2. Tra cứu thông tin bảng đấu các đội ")
    print('__3. Lịch thi đấu ')
    print('__00. Thoát ')
    m = int(input("Lựa chọn của bạn >>> "))

wc=1
while wc!=0:
  try:
    print("___Chào mừng bạn đến với phần mềm tra cứu Word Cup___")
    modau()
    while True:
        if m == 1:
            c = int(input("Ngày cần tra cứu (20->30): "))
            while True:
                d = int(input("1.Bảng A\n2.Bảng B\n3.Bảng C\n4.Bảng D\n5.Bảng E\n6.Bảng F\n7.Bảng G\n8.Bảng H\n0.Quay lại\nSố tương ứng với bảng cần tìm>>> "))
                if c >= 20 and c <= 30 and d >= 1 and d <= 8:
                    tracuuwc(c, d)
                elif d == 0:
                    modau()
                    break
                else:
                    print('[ERROR] Bạn nhập chưa đúng. Mời bạn nhập lại_________ ')

        elif m == 2:
            while True:
                print("Số tương ứng với bảng cần tìm>>> \n1.Bảng A\n2.Bảng B\n3.Bảng C\n4.Bảng D\n5.Bảng E\n6.Bảng F\n7.Bảng G\n8.Bảng H\n0.Quay lại")
                a = int(input("Bảng đấu Word Cup cần tra :  "))
                print('___________________________________________________')
                if a > 0 and a <= 8:
                    thongtinbangdau(a)
                elif a == 0:
                    modau()
                    break
                else:
                    print("[ERROR] Bạn nhập chưa đúng. Mời bạn nhập lại_________")
                print('___________________________________________________')

        elif m == 3:
            print('_____Lịch thi đấu theo bảng_____')
            while True:
                print("Số tương ứng với bảng cần tìm>>> \n1.Bảng A\n2.Bảng B\n3.Bảng C\n4.Bảng D\n5.Bảng E\n6.Bảng F\n7.Bảng G\n8.Bảng H\n0.Quay lại")
                b = int(input('>>>Lịch thi đấu Word Cup theo bảng cần tra :  '))
                if b > 0 and b <= 8:
                    if b == 1:
                        lichthidaubangA()
                    if b == 2:
                        lichthidaubangB()
                    if b == 3:
                        lichthidaubangC()
                    if b == 4:
                        lichthidaubangD()
                    if b == 5:
                        lichthidaubangE()
                    if b == 6:
                        lichthidaubangF()
                    if b == 7:
                        lichthidaubangG()
                    if b == 8:
                        lichthidaubangH()
                elif b == 0:
                    modau()
                    break
                else:
                    print("[ERROR] Bạn nhập chưa đúng. Mời bạn nhập lại_________")
        elif m==00:
            wc=0
            print('<<<Kết thúc chạy chương trình>>>')
            break
        else:
            print("[ERROR] Bạn nhập chưa đúng. Mời bạn nhập lại_________")
            modau()
  except:
    print('[ERROR] Bạn nhập chưa đúng cú pháp_________ ')
