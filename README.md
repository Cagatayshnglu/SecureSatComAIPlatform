
# 🚀 SecureSatComAIPlatform

Yapay zekâ destekli güvenli uydu haberleşme simülasyon platformu.  
AES şifreleme, BPSK modülasyon, AWGN kanal modeli ve BER analizi içerir.  
Makine öğrenmesine dayalı hata düzeltme ve FastAPI REST servisiyle desteklenmiştir.

---

## 🧩 Özellikler

- 🔐 **Şifreleme:** AES-CFB ile veri güvenliği + HMAC ile bütünlük doğrulama
- 📡 **Modülasyon:** BPSK modülasyonu & demodülasyonu
- 📶 **Kanal Simülasyonu:** AWGN üzerinden sinyal bozunumu modellemesi
- 📉 **Hata Oranı Analizi:** Bit Error Rate (BER) vs SNR grafikleri
- 🤖 **Makine Öğrenmesi (Placeholder):** Hata düzeltme modülü geliştirilebilir
- 🌐 **API:** FastAPI tabanlı uçtan uca şifreleme REST servisi
- 📓 **Notebook:** BER analizini görselleştiren Jupyter Notebook
- 🧪 **Modüler Kod:** `main.py` üzerinden uçtan uca simülasyon çalıştırılabilir

---

## ⚙️ Kurulum

```bash
git clone https://github.com/Cagatayshnglu/SecureSatComAIPlatform.git
cd SecureSatComAIPlatform
pip install -r requirements.txt
```

---

## 🚀 Kullanım

**Simülasyonu çalıştırmak için:**
```bash
python main.py
```

**API servisini başlatmak için:**
```bash
uvicorn api.app:app --reload
```

**Notebook ile analiz yapmak için:**
```bash
jupyter notebook notebooks/Simulation.ipynb
```

---

## 📁 Proje Yapısı

```
SecureSatComAIPlatform/
│
├── src/
│   ├── encryption/           # AES ve HMAC şifreleme
│   ├── modulation/           # BPSK modülasyon/demodülasyon
│   ├── channel/              # AWGN kanal simülasyonu
│   └── ml/                   # ML tabanlı hata düzeltme modülü (placeholder)
│
├── api/                      # FastAPI REST servisi
│   └── app.py
│
├── notebooks/                # BER analizi ve görselleştirme
│   └── Simulation.ipynb
│
├── main.py                   # Uçtan uca demo akış
├── requirements.txt          # Gerekli Python paketleri
├── README.md                 # Proje tanıtımı
└── LICENSE                   # MIT Lisansı
```

---

## 📜 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.

---

## 🤝 Katkıda Bulunma

Katkılar memnuniyetle kabul edilir! PR açmak veya issue bırakmak serbesttir.  
İletişim için: [Cagatayshnglu](https://github.com/Cagatayshnglu)
