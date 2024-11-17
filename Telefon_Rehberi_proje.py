import random
import time
import json

class TelefonRehberi:
    def __init__(self, rehber_dosya="rehber.json"):
        self.rehber_dosya = rehber_dosya
        self.rehber_durum = "Kapalı"
        self.rehber_listesi = self.rehberi_yukle()

    def rehberi_ac(self):
        if self.rehber_durum == "Açık":
            print("Rehber Zaten Açık...")
        else:
            print("Rehber Açılıyor...")
            time.sleep(1)
            print("Rehber Açıldı.")
            self.rehber_durum = "Açık"

    def rehberi_kapat(self):
        if self.rehber_durum == "Kapalı":
            print("Rehber Zaten Kapalı...")
        else:
            print("Rehber Kapanıyor...")
            time.sleep(1)
            print("Rehber Kapatıldı.")
            self.rehber_durum = "Kapalı"

    def rehberi_kaydet_json(self):
        with open(self.rehber_dosya, 'w') as dosya:
            json.dump(self.rehber_listesi, dosya, ensure_ascii=False, indent=4)

    def rehberi_yukle(self):
        try:
            with open(self.rehber_dosya, 'r') as dosya:
                return json.load(dosya)
        except FileNotFoundError:
            return []

    def __len__(self):
        return len(self.rehber_listesi)

    def __str__(self):
        if not self.rehber_listesi:
            return "Rehber Boş."
        rehber_bilgisi = "Kişi Listesi:\n"
        for kisi in self.rehber_listesi:
            rehber_bilgisi += f"- İsim: {kisi['isim']}, Numara: {kisi['numara']}\n"
        return rehber_bilgisi


class Islemler(TelefonRehberi):
    def kisi_ekle(self, isim, numara):
        for kisi in self.rehber_listesi:
            if kisi["isim"] == isim and kisi["numara"] == numara:
                print(f"{isim} isimli kişi zaten rehberde mevcut.")
                return
        if not numara.isdigit() or len(numara) != 10:
            print("Lütfen 10 haneli bir numara giriniz.")
            return
        print("Kişi Ekleniyor...")
        time.sleep(1)
        self.rehber_listesi.append({"isim": isim, "numara": numara})
        self.rehberi_kaydet_json()
        print(f"{isim} İsimli Kişi Eklendi.")

    def kisi_sil(self, isim):
        print("Kişi Siliniyor...")
        time.sleep(1)
        for kisi in self.rehber_listesi:
            if kisi["isim"] == isim:
                self.rehber_listesi.remove(kisi)
                self.rehberi_kaydet_json()
                print(f"{isim} isimli kişi silindi.")
                return
        print(f"{isim} isimli kişi bulunamadı.")

    def rastgele_kisi(self):
        if not self.rehber_listesi:
            print("Rehberde Kişi Yok.")
        else:
            rastgele_kisi = random.choice(self.rehber_listesi)
            print(f"Rastgele Seçilen Kişi: {rastgele_kisi['isim']} - {rastgele_kisi['numara']}")

    def rehberi_kaydet_txt(self, dosya_adi="rehber.txt"):
        with open(dosya_adi, 'w') as dosya:
            for kisi in self.rehber_listesi:
                dosya.write(f"İsim: {kisi['isim']}, Numara: {kisi['numara']}\n")
        print("Rehber dosya olarak kaydedildi.")


class Engellenenler(Islemler):
    def __init__(self):
        super().__init__("engellenenler.json")

    def kisi_engelle(self, isim, numara):
        print(f"{isim} isimli kişi engelleniyor...")
        time.sleep(1)
        self.rehber_listesi.append({"isim": isim, "numara": numara})
        self.rehberi_kaydet_json()
        print(f"{isim} isimli kişi engellendi.")

    def kisi_engeli_kaldir(self, isim):
        print(f"{isim} isimli kişinin engeli kaldırılıyor...")
        time.sleep(1)
        for kisi in self.rehber_listesi:
            if kisi["isim"] == isim:
                self.rehber_listesi.remove(kisi)
                self.rehberi_kaydet_json()
                print(f"{isim} isimli kişinin engeli kaldırıldı.")
                return
        print(f"{isim} isimli kişi engellenenler listesinde bulunamadı.")


class FavoriKisiler(Islemler):
    def __init__(self):
        super().__init__("favoriler.json")

    def favori_ekle(self, isim, numara):
        print(f"{isim} isimli kişi favorilere ekleniyor...")
        time.sleep(1)
        self.rehber_listesi.append({"isim": isim, "numara": numara})
        self.rehberi_kaydet_json()
        print(f"{isim} isimli kişi favorilere eklendi.")

    def favori_cikar(self, isim):
        print(f"{isim} isimli kişi favorilerden çıkarılıyor...")
        time.sleep(1)
        for kisi in self.rehber_listesi:
            if kisi["isim"] == isim:
                self.rehber_listesi.remove(kisi)
                self.rehberi_kaydet_json()
                print(f"{isim} isimli kişi favorilerden çıkarıldı.")
                return
        print(f"{isim} isimli kişi favorilerde bulunamadı.")


# Ana Program
rehber = Islemler()
engellenenler = Engellenenler()
favoriler = FavoriKisiler()

print("""
Telefon Rehberi Uygulaması

1. Rehberi Aç
2. Rehberi Kapat
3. Kişi Ekle
4. Kişi Sil
5. Kişi Sayısını Öğren
6. Rastgele Kişi Seç
7. Rehberi Görüntüle
8. Rehberi Kaydet
9. Rehberi Yükle
10. Engellenenler Menüsü
11. Favoriler Menüsü

Çıkmak için 'q' ya basın.
""")

while True:
    islem = input("İşlemi Seçiniz: ")

    if islem == "q":
        print("Program Sonlandırılıyor...")
        time.sleep(1)
        break
    elif islem == "1":
        rehber.rehberi_ac()
    elif islem == "2":
        rehber.rehberi_kapat()
    elif islem == "3":
        isim = input("Eklemek istediğiniz kişinin ismi: ")
        print("Numaranızın başına 0 eklemeden giriniz.")
        numara = input("Eklemek istediğiniz kişinin numarası: ")
        rehber.kisi_ekle(isim, numara)
    elif islem == "4":
        isim = input("Silmek istediğiniz kişinin ismi: ")
        rehber.kisi_sil(isim)
    elif islem == "5":
        print("Rehberdeki kişi sayısı:", len(rehber))
    elif islem == "6":
        rehber.rastgele_kisi()
    elif islem == "7":
        print(rehber)
    elif islem == "8":
        rehber.rehberi_kaydet_txt()
    elif islem == "9":
        rehber.rehberi_yukle()
        print("Rehber Yüklendi.")
    elif islem == "10":
        print("\nEngellenenler Menüsü")
        print("1. Kişi Engelle")
        print("2. Kişi Engeli Kaldır")
        print("3. Engellenenleri Göster")
        alt_islem = input("Seçiminizi yapın: ")
        if alt_islem == "1":
            isim = input("Engellenecek kişinin ismi: ")
            numara = input("Engellenecek kişinin numarası: ")
            engellenenler.kisi_engelle(isim, numara)
        elif alt_islem == "2":
            isim = input("Engeli kaldırılacak kişinin ismi: ")
            engellenenler.kisi_engeli_kaldir(isim)
        elif alt_islem == "3":
            print(engellenenler)
        else:
            print("Geçersiz seçim.")
    elif islem == "11":
        print("\nFavoriler Menüsü")
        print("1. Favorilere Ekle")
        print("2. Favorilerden Çıkar")
        print("3. Favorileri Göster")
        alt_islem = input("Seçiminizi yapın: ")
        if alt_islem == "1":
            isim = input("Favorilere eklenecek kişinin ismi: ")
            numara = input("Favorilere eklenecek kişinin numarası: ")
            favoriler.favori_ekle(isim, numara)
        elif alt_islem == "2":
            isim = input("Favorilerden çıkarılacak kişinin ismi: ")
            favoriler.favori_cikar(isim)
        elif alt_islem == "3":
            print(favoriler)
        else:
            print("Geçersiz seçim.")
    else:
        print("Geçersiz İşlem...")
