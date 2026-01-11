# BLM101 - Bilgisayar Mühendisliğine Giriş Dönem Projesi

## 👤 Öğrenci Bilgileri
* **Ad Soyad:** Sümeyra İLHAN
* **Öğrenci Numarası:** 24360859085
* **Bölüm:** Bilgisayar Mühendisliği
* **Grup:** 1. Grup (Veri Depolama ve Sayısal Sistemler)

---

## 📺 Proje Sunum Videosu
Aşağıdaki bağlantıya tıklayarak proje sunumunu ve kodun çalışma demosunu izleyebilirsiniz:

👉 **[YouTube Videomu İzlemek İçin Tıklayın](https://youtu.be/Li3CFO6aXRY?si=cxwBMtlyp9igzPDq)**

---

## 🛠️ Proje Açıklaması
Bu proje, **Sayısal Sistemler** ve **Veri Depolama** mantığını anlamak amacıyla geliştirilmiştir. Kullanıcıdan alınan onluk (decimal) bir sayıyı, Python'un hazır fonksiyonlarını (`bin()`, `hex()`) kullanmadan; tamamen matematiksel algoritmalarla **İkilik (Binary)** ve **Onaltılık (Hexadecimal)** sistemlere dönüştürür.

### 🧠 Çalışma Mantığı ve Algoritma
1. **İkilik Dönüşüm:** Sayı sürekli 2'ye bölünür ve kalanlar bir listede tutulup ters çevrilerek sonuç elde edilir.
2. **Onaltılık Dönüşüm:** Sayı 16'ya bölünür; kalanlar 10-15 arasındaysa karşılık gelen A, B, C, D, E, F harflerine atanır.
3. **Bellek Simülasyonu:** Elde edilen ikilik sonuç, 8-bitlik bir bellek yapısını temsil etmek amacıyla kutucuklar (`[0][1]...`) içerisinde görselleştirilir.

---

## 💻 Kurulum ve Çalıştırma
Kodun çalışması için bilgisayarınızda Python 3.x yüklü olmalıdır.
1. Klasördeki `kodlar` dizinine gidin.
2. Terminale şu komutu yazın:
   ```bash
   py lesson.py
