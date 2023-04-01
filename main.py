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


dosyanin_Adi = str(input("Excel Dosyasının Yolunu Girin: "))
dosya = pd.read_excel("Calisma_Sayfasi1.xlsx")  # Tablonuzun konumunu girin

api = "YOUR API KEY" # Google api keyi giriniz!!!!!




sutunun_adi = str(input("Verilerin Olduğu Sütunun Adını Girin: "))


find_latitude_longitude(analiz_sutun(sutunun_adi), api)