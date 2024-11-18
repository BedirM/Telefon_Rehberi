TelefonRehberi
------------------------
- rehber_dosya: str
- rehber_durum: str
- rehber_listesi: list
------------------------
+ rehberi_ac(): void
+ rehberi_kapat(): void
+ rehberi_kaydet_json(): void
+ rehberi_yukle(): list
+ __len__(): int
+ __str__(): str


          | 
          V 
Islemler (TelefonRehberi)
------------------------
+ kisi_ekle(isim: str, numara: str): void
+ kisi_sil(isim: str): void
+ rastgele_kisi(): void
+ rehberi_kaydet_txt(dosya_adi: str): void


          | 
          V 
Engellenenler (Islemler)
------------------------
+ kisi_engelle(isim: str, numara: str): void
+ kisi_engeli_kaldir(isim: str): void


          | 
          V 
FavoriKisiler (Islemler)
------------------------
+ favori_ekle(isim: str, numara: str): void
+ favori_cikar(isim: str): void
