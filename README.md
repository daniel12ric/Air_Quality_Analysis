# 🌫️ Dashboard Analisis Kualitas Udara (PM2.5)

Proyek ini merupakan bagian dari submission akhir kelas Dicoding: **Belajar Analisis Data dengan Python**. Dashboard ini dibuat menggunakan **Streamlit** dan bertujuan untuk mengeksplorasi dan memvisualisasikan kualitas udara (khususnya PM2.5) berdasarkan data historis.

## 📊 Fitur Dashboard

- Visualisasi tren rata-rata **PM2.5** per bulan untuk setiap stasiun dan tahun
- Heatmap korelasi antara **PM2.5** dan variabel cuaca lainnya seperti suhu, kelembaban, tekanan, dll
- Menampilkan lokasi stasiun dengan **tingkat PM2.5 tertinggi dan terendah**
- Insight dari data yang dianalisis

## 📁 Struktur Proyek

```
📦 air_quality_dashboard/
│
├── dashboard             
├────── air_quality.csv                              # Dataset hasil cleaning
├────── air_quality_app.py                           # File utama Streamlit             
├── data
├────── PRSA_Data_Aotizhongxin_20130301-20170228     # dataset kota
├────── PRSA_Data_Changping_20130301-20170228        # dataset kota
├────── PRSA_Data_Dingling_20130301-20170228         # dataset kota
├────── PRSA_Data_Dongsi_20130301-20170228           # dataset kota
├────── PRSA_Data_Guanyuan_20130301-20170228         # dataset kota
├────── PRSA_Data_Gucheng_20130301-20170228          # dataset kota
├────── PRSA_Data_Huairo_20130301-20170228           # dataset kota
├────── PRSA_Data_Nongzhanguan_20130301-20170228     # dataset kota
├────── PRSA_Data_Shunyi_20130301-20170228           # dataset kota
├────── PRSA_Data_Tiantan_20130301-20170228          # dataset kota
├────── PRSA_Data_Wanliu_20130301-20170228           # dataset kota
├────── PRSA_Data_Wanshouxigong_20130301-20170228    # dataset kota
├── requirements.txt                                 # Daftar library yang dibutuhkan
├── Proyek_Analisis_Data.ipynb                       # File ipynb untuk meneliti model sebelum dimasukkan dalam streamlit
└── README.md                                        # Dokumentasi proyek
```

## 🚀 Cara Menjalankan

1. **Clone / download** repositori ini
2. Install dependencies dengan:

   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan aplikasi:

   ```bash
   streamlit run dashboard/air_quality_app.py
   ```

## 🧪 Dataset

Dataset yang digunakan adalah kumpulan data kualitas udara yang mencakup parameter:
- PM2.5, PM10, SO2, NO2, CO, O3
- TEMP (suhu), PRES (tekanan), DEWP (dew point), RAIN, WSPM (wind speed)
- Timestamp dan lokasi stasiun

## 📌 Pertanyaan Bisnis yang Dijawab

1. **Bagaimana tren rata-rata PM2.5 dari waktu ke waktu (per bulan)?**
2. **Stasiun mana yang memiliki tingkat PM2.5 tertinggi dan terendah?**

## 💡 Insight

- Kualitas udara cenderung **memburuk pada musim dingin** (Desember–Januari).
- PM2.5 memiliki korelasi yang kuat dengan PM10.
- Faktor cuaca seperti suhu dan kecepatan angin ikut mempengaruhi kadar polusi.

## 👨‍💻 Author

Daniel Darren Richardo - Dicoding Submission  
Tahun: 2025