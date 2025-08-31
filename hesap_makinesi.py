soru1 = input("hangi sayı ile işlem yapmak istiyorsun?: ")
islem = input("yapmak istediğiniz işlemi seçin:")
soru2 = input("ikinci sayıyı girin:")

if islem == "+":
    print(int(soru1) + int(soru2))

elif islem == "-":
    print(int(soru1) + int(soru2))

elif islem == "*":
    print(int(soru1) * int(soru2))

elif islem == "/":
    print(int(soru1) / int(soru2))
    if int(soru1) / int(soru2) != 0:
        print("sıfırı bölemezsin!") #sıfırı ikinci sayıyla bölmeye çalışınca sonsuz döngüye giriyor ve ilk sayıyı sıfıra bölüncede hata veriyor yardım eddebirmisiniz buna :(
    else:
        while True:
            print("lütfen işlem seç")
