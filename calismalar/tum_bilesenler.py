from tkinter import*
ekran=Tk()
ekran.title("Birinci")
ekran.geometry("600x600+300+300")


ilkfiyat=Label(text="ALIŞ FİYATI")
ilkfiyat.grid(row=0,column=0)

fgir=Entry()
fgir.grid(row=1,column=0)

vergi=IntVar()
vergihesap=0
karhesap=0
toplam=0

def hesapla():
    if vergi.get()==1:
        vergihesap=int(fgir.get())*1/100
        print(vergihesap)
    if vergi.get()==2:
        vergihesap=int(fgir.get())*8/100
        print(vergihesap)
    if vergi.get()==3:
        vergihesap=int(fgir.get())*18/100
        print(vergihesap)
    if kar.get()==1:
        karhesap=int(fgir.get())*10/100
        print(karhesap)
    if kar.get()==2:
        karhesap=int(fgir.get())*20/100
        print(karhesap)
    if kar.get()==3:
        karhesap=int(fgir.get())*30/100
        print(karhesap)
    toplam=int(fgir.get())+vergihesap+karhesap
    print(toplam)
    sonfiyat["text"]="ÜRÜNÜN SON FİYATI:"+str(toplam)
    vergideger["text"]="ÜRÜNÜN VERGİ ORANI:"+str(vergihesap)
    kardeger["text"]="ÜRÜNDEN ELDE EDİLEN KAR:"+str(karhesap)

def yap():
    pass

voran=Label(text="Vergi oranı")
voran.grid(row=0,column=1)

v1=Radiobutton(ekran,text="%1",variable=vergi,value=1,command=yap)
v1.grid(row=1,column=1)

v8=Radiobutton(ekran,text="%8",variable=vergi,value=2,command=yap)
v8.grid(row=2,column=1)

v18=Radiobutton(ekran,text="%18",variable=vergi,value=3,command=yap)
v18.grid(row=3,column=1)

kar=IntVar()
koran=Label(text="Kar oranı")
koran.grid(row=0,column=2)

k10=Radiobutton(ekran,text="%10",variable=kar,value=1,command=yap)
k10.grid(row=1,column=2)

k20=Radiobutton(ekran,text="%20",variable=kar,value=2,command=yap)
k20.grid(row=2,column=2)

k30=Radiobutton(ekran,text="%30",variable=kar,value=3,command=yap)
k30.grid(row=3,column=2)


sonfiyat=Label(text="ÜRÜNÜN SON FİYATI")
sonfiyat.grid(row=4,column=1)
vergideger=Label(text="ÜRÜNÜN VERGİSİ")
vergideger.grid(row=5,column=1)
kardeger=Label(text="ÜRÜNDEN ELDE EDİLEN KAR")
kardeger.grid(row=6,column=1)


hesap=Button(text="HESAPLA",command=hesapla)
hesap.grid(row=7,column=1)










