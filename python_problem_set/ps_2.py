import re
def mailDogrula(mail,uzanti):
  if ( uzanti == 1):
    return re.match(r"[\w-]{0,20}@\w{2,20}",mail)
  elif (uzanti == 2):
    return re.match(r"[\w-]{0,20}@\w{2,20}\.\w{2,20}",mail)
  elif (uzanti ==3):
    return re.match(r"[\w-]{0,20}@\w{2,20}\.\w{2,20}\.\w{2,3}$",mail)
  else:
    print("Hatalı mail adresi girdiniz.")

uzt = int(input("@ işaretinden sonraki uzunluğu giriniz:"))
eposta = input("e-postanızı giriniz:")

gecerli = mailDogrula(eposta,uzt)
if gecerli:
  print("Mail adresiniz doğrudur.")
else:
  print("Mail adresiniz hatalıdır.")
