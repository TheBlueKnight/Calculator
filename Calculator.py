
print("""************************

1.Toplama İşlemi

2.Çıkarma İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi

************************
""")

a=float(input("İlk Sayıyı Giriniz:"))
b=float(input("İkinci Sayıyı Giriniz:"))


x=int(input("Yapmak İstedğiniz İşlem İçin 1-4 Arası Bir Sayı Giriniz: "))

if(x==1):
    print("Toplam={}".format(a+b))
if(x==2):
    print("Toplam={}".format(a-b))
if(x==3):
    print("Toplam={}".format(a*b))
if(x==4):
    print("Toplam={}".format(a/b))

else:
    print("Lütfen 1-4 Arası Bir Sayı Giriniz!!")
    

