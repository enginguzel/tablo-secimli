
print ("╔════════════════════════════╗")
print ("║       VEKTOREL APP         ║")
print ("╠════════════════════════════╣")
print ("║  1- hesaplamalar           ║")
print ("║  2- Oyunlar                ║")
print ("║  3- çziimler               ║")
print ("║  4- geziler                ║")
print ("║  5- çıkış                  ║")
print ("╚════════════════════════════╝")
secim = input("seciminiz nedir?")
if secim == "1" :
    print(secim, "sectiniz")
    print("hesaplamalar bölümüne yönlendirileceksiniz")
    import moduller1.hesapmodulu
    secim = input("seciminiz nedir?")
    if secim == "1" :
        print(secim, "sectiniz")
        print("toplama bölümüne yönlendirileceksiniz")
    elif secim == "2" :
        print(secim, "sectiniz")
        print("alan hesaplama bölümüne yönlendirileceksiniz")
    elif secim == "3" :
        print(secim, "sectiniz")
        print("çarpım bölümüne yönlendirileceksiniz")
    elif secim == "4" :
        print(secim, "sectiniz")
        print("bölme hesaplama bölümüne yönlendirileceksiniz")
    elif secim == "5" :
        print(secim, "sectiniz")   
        print("cikis yaptiniz, program kapatiliyor") 


elif secim == "2" :
    print(secim, "sectiniz")
    print("oyunlar bölümüne yönlendirileceksiniz")
    import moduller1.oyunmodulu
    secim = input("seciminiz nedir?")
    if secim == "1" :
        print(secim, "sectiniz")
        print("puan toplama bölümüne yönlendirileceksiniz")
    elif secim == "2" :
        print(secim, "sectiniz")
        print("bölüm oluşturma bölümüne yönlendirileceksiniz")
    elif secim == "3" :
        print(secim, "sectiniz")
        print("çgeçilen bölümler bölümüne yönlendirileceksiniz")
    elif secim == "4" :
        print(secim, "sectiniz")
        print("kaybedilen bölümler bölümüne yönlendirileceksiniz")
    elif secim == "5" :
        print(secim, "sectiniz")   
        print("cikis yaptiniz, program kapatiliyor") 

elif secim == "3" :
    print(secim, "sectiniz")
    print("çizimler bölümüne yönlendirileceksiniz")
    import moduller1.cizimmodulu
    secim = input("seciminiz nedir?")
    if secim == "1" :
        print(secim, "sectiniz")
        print("düz cizgiler bölümüne yönlendirileceksiniz")
    elif secim == "2" :
        print(secim, "sectiniz")
        print("yamuk cizgiler bölümüne yönlendirileceksiniz")
    elif secim == "3" :
        print(secim, "sectiniz")
        print("capraz cizgiler bölümüne yönlendirileceksiniz")
    elif secim == "4" :
        print(secim, "sectiniz")
        print("paralel cizgiler bölümüne yönlendirileceksiniz")
    elif secim == "5" :
        print(secim, "sectiniz")   
        print("cikis yaptiniz, program kapatiliyor") 

elif secim == "4" :
    print(secim, "sectiniz")
    print("geziler bölümüne yönlendirileceksiniz")    
    import moduller1.gezimodulu
    secim = input("seciminiz nedir?")
    if secim == "1" :
        print(secim, "sectiniz")
        print("planlanan geziler bölümüne yönlendirileceksiniz")
    elif secim == "2" :
        print(secim, "sectiniz")
        print("gidilecek yerler bölümüne yönlendirileceksiniz")
    elif secim == "3" :
        print(secim, "sectiniz")
        print("gidilen yerler bölümüne yönlendirileceksiniz")
    elif secim == "4" :
        print(secim, "sectiniz")
        print("kgidilmeyecek yerler bölümüne yönlendirileceksiniz")
    elif secim == "5" :
        print(secim, "sectiniz")   
        print("cikis yaptiniz, program kapatiliyor") 

elif secim == "5" :
    print (secim, "sectiniz")
    print ("cikis yaptiniz, program kapatiliyor")

