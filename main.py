import geocoder
import pandas as pd


def analiz_sutun(x):  # Belirtilen Sütunlardaki Verileri Bir Tablo Listesine Ekliyoruz
    tablo = []

    for i in range(len(dosya.index)):
        tablo.append(dosya.loc[[i], x].values[0])
        i += 1
    return tablo

def find_latitude_longitude(analiz_sutun, api): # analiz_sutun() fonksiyonunda topladığımız verilerin burada konumlarını buluyoruz
    
    latitude_longitude = []
     

    
    for i in analiz_sutun:
        
        g = geocoder.google(i , key = api )
        latitude_longitude.append(g.latlng)
        print(i)


    data = { "Latitude and Longitude":latitude_longitude}

    df = pd.DataFrame(data)

    print(df)

    while True:

      try:
        yesNo = str(input("Sonucu Excel Tablosu Olarak İster Misiniz? [E/H]"))

        if (yesNo == "E"):
          outputName = input("Dosyanın Adı Ne Olsun?")
          df.to_excel(outputName+".xlsx") 
          print("Dosyanız Oluşturuldu!" + outputName+".xlsx")
          break

        elif (yesNo == "H"):
          break

      except NameError:
        print("Geçersiz Seçim")



input_Api = input("Google API key giriniz: ")
api = input_Api # Google api keyi giriniz!!!!!

while True:

  try:
    dosyanin_Adi = str(input("Excel Dosyasının Yolunu Girin: "))
    dosya = pd.read_excel(dosyanin_Adi)  # Tablonuzun konumunu girin

    df = pd.DataFrame(dosya)

    print(df.head())
    break
  except FileNotFoundError:
    print("Dosya Bulunamadı")


sutunun_adi = str(input("Adres Verilerin Olduğu Sütunun Adını Girin: "))



find_latitude_longitude(analiz_sutun(sutunun_adi), api)