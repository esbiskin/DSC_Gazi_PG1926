from math import *
def toplama(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def carpma(a,b):
    return a * b
def bölme(a,b):
    return a / b
def karealma():
  karesialınan=float(input("Karesi Alınacak Sayı:"))
  karesi=karesialınan**2
  print(karesi)
def hipotenus():
  firstdik=float(input("Dik Kenarın 1.si:"))
  seconddik=float(input("Dik Kenarın 2.si:"))
  hipo=(firstdik*firstdik+seconddik*seconddik)**0.5
  print(hipo)
def kupcevre():
  karekenar=float(input("Küpün Herhangi Bir Kenarını Giriniz:"))
  karekenarcevre=6*(karekenar**2)
  print(karekenarcevre)
def kupalan():
    karekenara = float(input("Küpün Herhangi Bir Kenarını Giriniz:"))
    karekenaralan = karekenara ** 3
    printAlan("Küp", karekenaralan)
def dairecevre():
    pi = float(input("Varsayılan Pi:"))
    dairer = float(input("Yarıçapı Giriniz:"))
    dairecevresonuc = 2 * pi * dairer
    print(dairecevresonuc)
def dairealan():
    pi = float(input("Varsayılan Pi:"))
    dairer = float(input("Yarıçapı Giriniz:"))
    dairealansonuc = (pi) * (dairer ** 2)
    printAlan("Daire", dairealansonuc)

print("**********************************************\n"
      "GELİŞMİŞ HESAP MAKİNESİ PROGRAMI \n"
      "LÜTFEN İŞLEM SEÇİN\n"
      "1. İşlem = Toplama \n"
      "2. İşlem = Çıkarma \n"
      "3. İşlem = Çarpma \n"
      "4. İşlem = Bölme \n"
      "5. İşlem = Kare Alma \n"
      "6. İşlem = Faktoriyel \n"
      "7. İşlem = Hipotenüs \n"
      "8. İşlem = Küp Çevre Hesaplama \n"
      "9. İşlem = Küp Alan Hesaplama \n"
      "10. İşlem = Daire Çevre Hesaplama \n"
      "11. İşlem = Daire Alan Hesaplama \n"
           "**********************************************\n")
islem = input("işlem seçiniz :")
while True:

    if(islem=="q"):
        print("Çıkış Yaptınız!!! Tekrar Çalıştırın!!!")
        break
    elif(islem=="1"):
        a = int(input("birinci sayı: "))
        b = int(input("ikinci sayı: "))
        print(toplama(a,b))
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    elif(islem=="2"):
        a = int(input("birinci sayı: "))
        b = int(input("ikinci sayı: "))
        print(cıkarma(a, b))
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    elif (islem == "3"):
        a = int(input("birinci sayı: "))
        b = int(input("ikinci sayı: "))
        print(carpma(a, b))
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    elif (islem == "4"):
        a = int(input("birinci sayı: "))
        b = int(input("ikinci sayı: "))
        print(bölme(a, b))
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    elif(islem=="5"):
        karealma()
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    elif(islem=="6"):
        faktöriyel = int(input("Faktöriyel'i alınacak sayıyı giriniz: "))
        faktöriyel_sonuc = factorial(faktöriyel)
        print(faktöriyel_sonuc)
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    elif(islem=="7"):
        hipotenus()
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    elif(islem=="8"):
        kupcevre()
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    elif(islem=="9"):
        kupalan()
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    elif(islem=="10"):
        dairecevre()
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    elif(islem=="11"):
        dairealan()
        print("İşlem Bitti! Tekrar işlem yapmak için programı tekrar çalıştırınız.")
        break
    else:
        print("Geçersiz İşlem Yaptınız!! Lüfen Tekrar Deneyin!!!")
        
