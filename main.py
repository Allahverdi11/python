##r = float(input("raidusu yazin :" ))
#print("dairenin sahesi: " + str(pi * r **2))
#a, b, c = 2, 5,10
#x = float(input("x : "))
#y = float(input("y:  "))
#sonuc = (x*y)-(a+b+c)
#sonuc = c//b
#sonuc = b**a
#sayilar = 1,5,7,10,3
##netice = c**3



          

#print(netice) 

#sonuc = int(input("sayi1 icin tam sayi giriniz :" ))
#sonuc1 = int(input("sayi2 icin tam sayi giriniz:"))
#print(sonuc>sonuc1)

#sayi = int(input("tam bir sayi giriniz:"))

#if sayi %2 == 0 : 
  #print("sayiniz cift")
#sinav1 = float(input("not:"))
#sinav2 = float(input("not:"))
#sonuc1 = (sinav1*50)/100
#sonuc2 = (sinav2 * 40)/100
#sonuc3 = float(sonuc1 +sonuc2)
#if sonuc1+sonuc2 > 50:
 # print(f"Tebrikler Sinavdan gectiniz, notunuz:{sonuc3}")


#elif sonuc1+sonuc2 < 50:
  #print(f"Maalesef dersten kaldiniz, notunuz: {sonuc3}")
#x = float(input("sayi giriniz:"))
#sonuc =((x>50) and (x<100)) and x%2==1
#print(sonuc)

#2
##_parol = "12345"
#email = str(input("kullanici adini giriniz:"))
#parol = str(input("parolani yaziniz: "))
#sonuc = (_email==email) and (_parol == parol)
#print(sonuc)

#3
#sayi1 = float(input("sayi1 gir: "))
#sayi2 = float(input("sayi2 gir: "))
#sayi3 = float(input("sayi3 gir: "))
#sonuc= sayi1>sayi2>sayi3
#sonuc1 = sayi1<sayi2
#sonuc2 = sayi2<sayi3
#sonuc3 = sayi1<sayi3
#print(sonuc, sonuc1, sonuc2,sonuc3)

#4
#vize1 = float(input("vize1 sonuc: "))
#vize2 = float(input("vize2 sonuc: "))
#final = float(input("final sonuc: "))
#sonuc1 = float((vize1+vize2+final)/3)
#if float(sonuc1)>50 and float(final)> 70 :
 # print(f"Tebrikler, sinavdan gectiniz, notunuz : {sonuc1}")

#elif float(sonuc1)<=50 or float(final)<70:
 # print(f"Maalesef, malsiniz, not ortalamaniz: {sonuc1}")

#5


#ad = str(input("adiniz : "))
#soyad = str(input("soyadiniz: "))
#yas = int(input("yasiniz: "))
#print(f"Menim adim {ad} {soyad}  ve  menim {yas} yasim var.")


# id = input('oyuncu id: ')
 ##nationality = input("ülke: ")
 #yearOfBirth = input('doğum yılı: ')
#current_team = input('takım: ')
# history = input('oynadığı yerler: ')

#players.update({
 #   id: {
   #   "name": name,
  #    "yearOfBirth": yearOfBirth,
   #   "nationality": nationality,
  #    "yearOfBirth": yearOfBirth,
 #     "current_team": current_team,
#      "history": history.split(',')
 #  }
#3})
#print(players)
#urunler = {}
##ad = input(" ad : ")
#fiyat = input("fiyat : ")
#urunler[id] = {"ad" : ad, 
           #  "fiyat" : fiyat }


#id = input (" id : ")
#ad = input(" ad : ")
#fiyat = input("fiyat : ")
#urunler[id] = {"ad" : ad, 
    #         "fiyat" : fiyat }
#id = input("aramak istediginiz urun id : ")
#urun = urunler[id]
#print(urun)

#urun_bilgisi= {"id": , "ad":, "fiyat":}
#print(urun_bilgisi)'

##now = datetime.datetime.now()
#print ("Current date and time : ")
#print (now.strftime("%Y-%m-%d %H:%M:%S"))  """

#sayi = float(input("Bir sayi giriniz: "))
#if sayi > 50 and sayi < 100 :
# print("dogru aralik")
#elif sayi< 50 or sayi > 100:
 # print("yanlis aralik")

sayi = float(input("Bir sayi giriniz: "))
if sayi>0 and (sayi%2 == 0 ):
  print("pozitif cift sayi")
elif sayi<0 and (sayi %2== 0):
  print("negatif, cift sayi")
elif sayi>0 and (sayi %2==1):
  print("pozitif, tek sayi")
elif sayi<0 and (sayi%2==1):
  print("negatif, tek sayi")
if sayi==0 and (sayi%2==0):
  print("ne negatif, ne pozitif")

