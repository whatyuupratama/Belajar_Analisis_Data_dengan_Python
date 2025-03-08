```markdown
# Proyek Analisis Sewa Sepeda dari Dataset Bike Sharing

Proyek ini bertujuan untuk menganalisis data penggunaan sepeda berbagi dari dataset yang berisi informasi tentang sewa sepeda setiap hari dan setiap jam. Visualisasi dan analisis dilakukan menggunakan berbagai alat Python seperti **Pandas**, **Seaborn**, **Matplotlib**, dan **Streamlit** untuk membangun dashboard interaktif.

## Fitur Proyek

- **Analisis Data**: Menggunakan file CSV yang berisi data penggunaan sepeda dan menghasilkan insight terkait tren penggunaan berdasarkan waktu dan musim.
- **Dashboard Interaktif**: Membangun dashboard interaktif menggunakan **Streamlit** untuk visualisasi data sewa sepeda dalam bentuk grafik yang dapat disesuaikan.
- **Proses Extract Data**: Memanfaatkan file ZIP untuk mengekstrak dataset yang digunakan dalam analisis.

## Struktur Proyek
```

project/
├── dashboard/
│ ├── streamlit.py # File utama untuk aplikasi Streamlit
│ └── data/
│ ├── day.csv # Data sewa sepeda per hari
│ └── hour.csv # Data sewa sepeda per jam
├── Proyek_Analisis_Data.ipynb # Notebook analisis data
└── requirements.txt # Daftar dependensi Python

````

## Persyaratan

Sebelum memulai, pastikan Anda telah menginstal dependensi yang diperlukan. Anda bisa menggunakan `pip` untuk menginstal semua paket yang dibutuhkan dengan menjalankan:

```bash
pip install -r requirements.txt
````

Berikut adalah daftar pustaka yang digunakan dalam proyek ini:

- pandas: Untuk manipulasi data
- numpy: Untuk perhitungan numerik
- matplotlib: Untuk visualisasi data
- seaborn: Untuk visualisasi statistik yang lebih menarik
- plotly: Untuk grafik interaktif
- streamlit: Untuk membangun dashboard interaktif

## Menjalankan Proyek

**Langkah 1: Ekstrak Data**

Proyek ini menggunakan data yang dikemas dalam file ZIP. Pastikan file ZIP berada di folder `dashboard/` dan memiliki nama `Bike-sharing-dataset.zip`. Ekstrak data dengan menjalankan kode Python berikut di notebook Anda (`Proyek_Analisis_Data.ipynb`):

```python
import zipfile
import os

zip_file = "dashboard/Bike-sharing-dataset.zip"
extract_folder = "dashboard/data"  # Pastikan diekstrak ke dalam folder `data` di bawah `dashboard`

os.makedirs(extract_folder, exist_ok=True)

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)
```

Skrip ini akan mengekstrak file CSV ke dalam folder `dashboard/data/`. **Pastikan folder `data` berada di bawah folder `dashboard`**.

**Langkah 2: Menjalankan Aplikasi Streamlit**

Untuk menjalankan dashboard interaktif, gunakan perintah berikut di terminal:

```bash
streamlit run dashboard/streamlit.py
```

Ini akan membuka aplikasi Streamlit di browser Anda, di mana Anda dapat berinteraksi dengan grafik dan melihat tren sewa sepeda berdasarkan waktu, musim, dan variabel lainnya.

**Langkah 3: Menjalankan Notebook untuk Analisis Data**

Jika Anda ingin melakukan analisis data secara lebih mendalam, buka dan jalankan notebook `Proyek_Analisis_Data.ipynb` di Jupyter Notebook atau Google Colab. Di dalam notebook ini, Anda akan menemukan analisis data yang dilakukan pada dataset, termasuk visualisasi tren sewa sepeda per jam dan per hari.

## Visualisasi di Streamlit

Aplikasi Streamlit memungkinkan Anda untuk melihat grafik tren sewa sepeda dengan mudah. Berikut adalah beberapa contoh visualisasi utama:

- Jumlah Sewa Berdasarkan Jam: Menampilkan tren sewa sepeda berdasarkan waktu dalam sehari.
- Jumlah Sewa Berdasarkan Bulan: Visualisasi tren musiman berdasarkan bulan.

## Cara Mengembangkan Proyek

Jika Anda ingin mengembangkan proyek ini lebih lanjut, berikut beberapa langkah yang dapat dilakukan:

- Menambahkan lebih banyak analisis dan visualisasi data.
- Menggunakan Plotly untuk grafik interaktif lainnya.
- Menambahkan kontrol interaktif di Streamlit, seperti dropdown atau slider, untuk memfilter data berdasarkan kolom tertentu (misalnya, memilih musim atau hari tertentu).
- Meningkatkan model prediksi untuk meramalkan sewa sepeda di masa depan.

## Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat [LICENSE](LICENSE) untuk detail lebih lanjut.

```

**Perubahan dan Penjelasan:**

*   **Struktur Proyek:** Memastikan struktur folder jelas dan akurat.
*   **Kode Ekstraksi:** Memastikan kode ekstraksi ZIP mengekstrak file ke lokasi yang tepat (`dashboard/data`).  Ini adalah *kritis* untuk menghindari error path saat menjalankan aplikasi Streamlit.
*   **Penekanan Lokasi Data:** Menekankan pentingnya folder `data` berada *di bawah* folder `dashboard`.
*   **Tata Bahasa dan Kejelasan:**  Memperbaiki beberapa kesalahan tata bahasa dan membuat penjelasan lebih jelas.
*   **Link Lisensi:** Menambahkan link placeholder untuk file LICENSE (jika ada).
*   **Pemformatan Kode:** Memastikan kode (Python dan Bash) diformat dengan benar untuk kejelasan.

Salin seluruh konten di atas ke file `README.md` Anda.  Pastikan file `Bike-sharing-dataset.zip` berada di folder `dashboard/` dan file CSV diekstrak ke `dashboard/data/`.  Setelah itu, perintah `streamlit run dashboard/streamlit.py` seharusnya berfungsi.
```
