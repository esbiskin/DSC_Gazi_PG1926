import math
#**********ERTUĞRUL SAMET BİŞKİN - 401371*************#
sec=int(input("Kare Hesaplamaları İçin '1' \nDikdörtgen Hesaplamaları İçin '2' \nHareketli Bir Cismin Hız Formülü Hesaplamaları İçin '3' \nİvme Formülü Hesaplamaları İçin '4' \nKatılarda Yüzeye Yapılan Basınç Formülü Hesaplamaları İçin '5' Giriniz="))
#****************************************************#
if sec==1:
    def kare():
        s1=int(input("Karenin Alanını Bulmak İçin '1' \nKarenin Kenar Uzunluğunu Bulmak İçin '2' Giriniz="))

        if s1==1:
            s2=int(input("Karenin Kenar Uzunluğunu Giriniz="))
            hesapla=s2*s2
            print("Karenin Alanı= ",hesapla)

        else:
            s3=int(input("Karenin Alanını Giriniz="))
            hesapla2=math.sqrt(s3)
            print("Karenin Bir Kenar Uzunluğu= ",hesapla2)
    kare()
#****************************************************#
if sec==2:
    def dikdortgen():
        s1=int(input("Dikdörtgenin Alanını Bulmak İçin '1' \nDikdörtgenin Uzun Kenar Uzunluğunu Bulmak İçin '2' \nDikdörtgenin Kısa Kenar Uzunluğunu Bulmak İçin '3' Giriniz="))

        if s1==1:
            s2=int(input("Dikdörtgenin Uzun Kenar Uzunluğunu Giriniz="))
            s3=int(input("Dikdörtgenin Kısa Kenar Uzunluğunu Giriniz="))
            hesapla=s2*s3
            print("Dikdörtgenin Alanı= ",hesapla)

        if s1==2:
            s4=int(input("Dikdörtgenin Alanını Giriniz="))
            s3=int(input("Dikdörtgenin Kısa Kenar Uzunluğunu Giriniz="))
            hesapla2=s4/s3
            print("Dikdörtgenin Uzun Kenar Uzunluğu= ",hesapla2)

        if s1==3:
            s4=int(input("Dikdörtgenin Alanını Giriniz="))
            s2=int(input("Dikdörtgenin Uzun Kenar Uzunluğunu Giriniz="))
            hesapla3=s4/s2
            print("Dikdörtgenin Kısa Kenar Uzunluğu= ",hesapla3)
    dikdortgen()
#****************************************************#
if sec==3:
    def hareketli():
        s1=int(input("Hızı Bulmak İçin '1' \nYolu Bulmak İçin '2' \nZamanı Bulmak İçin '3' Giriniz="))

        if s1==1:
            s2=int(input("Yolu Giriniz= "))
            s3=int(input("Zamanı Giriniz= "))
            hesapla=s2/s3
            print("Hız= ",hesapla)

        if s1==2:
            s4=int(input("Hızı Giriniz= "))
            s3=int(input("Zamanı Giriniz= "))
            hesapla2=s4*s3
            print("Yol= ",hesapla2)

        if s1==3:
            s2=int(input("Yolu Giriniz= "))
            s4=int(input("Hızı Giriniz= "))
            hesapla3=s2/s4
            print("Zaman= ",hesapla3)
    hareketli()
#****************************************************#
if sec==4:
    def ivme():
        s1=int(input("İvmeyi Bulmak İçin '1' \nHız Değişimini Bulmak İçin '2' \nZamanı Bulmak İçin '3' Giriniz="))

        if s1==1:
            s2=int(input("Hız Değişimini Giriniz= "))
            s3=int(input("Zamanı Giriniz= "))
            hesapla=s2/s3
            print("İvme= ",hesapla)

        if s1==2:
            s4=int(input("İvmeyi Giriniz= "))
            s3=int(input("Zamanı Giriniz= "))
            hesapla2=s4*s3
            print("Hız Değişimi= ",hesapla2)

        if s1==3:
            s2=int(input("Hız Değişimini Giriniz= "))
            s4=int(input("İvmeyi Giriniz= "))
            hesapla3=s2/s4
            print("Zaman= ",hesapla3)
    ivme()
#****************************************************#
if sec==5:
    def basınc():
        s1=int(input("Basıncı Bulmak İçin '1' \nKuvveti Bulmak İçin '2' \nYüzey Alanını Bulmak İçin '3' Giriniz="))

        if s1==1:
            s2=int(input("Kuvveti Giriniz= "))
            s3=int(input("Yüzey Alanını Giriniz= "))
            hesapla=s2/s3
            print("Basınç= ",hesapla)

        if s1==2:
            s4=int(input("Basıncı Giriniz= "))
            s3=int(input("Yüzey Alanını Giriniz= "))
            hesapla2=s4*s3
            print("Kuvvet= ",hesapla2)

        if s1==3:
            s2=int(input("Kuvveti Giriniz= "))
            s4=int(input("Basıncı Giriniz= "))
            hesapla3=s2/s4
            print("Yüzey Alanı= ",hesapla3)
    basınc()
