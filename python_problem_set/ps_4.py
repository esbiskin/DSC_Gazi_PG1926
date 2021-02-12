numb=[]
a=0
sayac=0
sayi=int(input("sayi gir: "))
max=sayi
while a<4:
  sayi=int(input("sayi gir: "))
  numb.append(sayi)
  
  if (sayi > max) and (sayi%2==1):
    max=sayi
    
  a+=1
print(max)
