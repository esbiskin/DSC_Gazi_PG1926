
sonmaas=0
def netmaas(brut,vor,prim):
    sonmaas=brut-(brut*vor/100)+prim
    print("brut maas=",brut,"vergi oranı=",brut*vor/100,"prim=",prim,"son maas=",sonmaas)

netmaas(1000,20,250)
