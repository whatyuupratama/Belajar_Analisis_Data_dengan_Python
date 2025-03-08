```markdown
# 🚲 Analisis Sewa Sepeda 📊

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-orange.svg)](https://streamlit.io/)

Proyek ini menganalisis data sewa sepeda harian & per jam untuk insight & visualisasi interaktif.

## 🚀 Fitur Utama

- **Analisis Data:** Insight tren sewa berdasarkan waktu & musim.
- **Dashboard Interaktif:** Visualisasi data dengan Streamlit.
- **Ekstraksi Otomatis:** Mengekstrak data dari file ZIP.

## 🗂️ Struktur Proyek
```

project/
├── dashboard/
│ ├── streamlit.py
│ └── Bike-sharing-dataset.zip
└── data/
│ ├── day.csv
│ └── hour.csv
├── Proyek_Analisis_Data.ipynb
└── requirements.txt

````

## 🛠️ Setup Environment

1.  **Clone Repository:**  Gunakan perintah berikut untuk mengkloning repositori ke komputer Anda. Ganti `https://github.com/whatyuupratama/Belajar_Analisis_Data_dengan_Python.git` dengan URL repositori Anda:

    ```bash
    git clone https://github.com/whatyuupratama/Belajar_Analisis_Data_dengan_Python.git
    ```

2.  **Masuk ke direktori proyek:** Setelah kloning selesai, masuk ke direktori proyek dengan perintah `cd`:

    ```bash
    cd Belajar_Analisis_Data_dengan_Python
    ```

3.  **Buat virtual environment (opsional):** Disarankan untuk membuat virtual environment agar dependensi proyek terisolasi:

    ```bash
    python3 -m venv venv
    ```

4.  **Aktifkan virtual environment:** Aktifkan virtual environment sesuai dengan sistem operasi Anda:

    *   Linux/MacOS:
        ```bash
        source venv/bin/activate
        ```
    *   Windows:
        ```bash
        .\venv\Scripts\activate
        ```

5.  **Install dependencies:** Install dependensi proyek menggunakan `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Menjalankan Proyek

1.  **Ekstrak Data:** Jalankan kode Python di notebook `Proyek_Analisis_Data.ipynb`:

    ```python
    import zipfile
    import os

    zip_file = "dashboard/Bike-sharing-dataset.zip"
    extract_folder = "dashboard/data"
    os.makedirs(extract_folder, exist_ok=True)

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    ```

    Pastikan `Bike-sharing-dataset.zip` ada di `dashboard/` dan diekstrak ke `dashboard/data/`.

2.  **Jalankan Streamlit:** `streamlit run dashboard/streamlit.py`

3.  **Analisis Data:** Buka & jalankan `Proyek_Analisis_Data.ipynb`.

## 📈 Visualisasi di Streamlit

*   Sewa per Jam
*   Tren Musiman

## 🔮 Pengembangan Lanjutan

*   Visualisasi Plotly
*   Filter Interaktif
*   Model Prediksi Sewa

## 📄 Lisensi

[MIT License](LICENSE)
````

**Perubahan Utama:**

- **Instruksi Kloning yang Jelas:** Menambahkan instruksi langkah demi langkah tentang cara mengkloning repositori menggunakan `git clone` dengan URL repositori yang diberikan.
- **Nama Direktori Proyek:** Memastikan bahwa `cd` menggunakan nama direktori proyek yang benar (`Belajar_Analisis_Data_dengan_Python`).
- **Penjelasan Tambahan:** Memberikan sedikit lebih banyak konteks untuk beberapa langkah, terutama yang terkait dengan virtual environment.

Sekarang, dengan asumsi tidak ada masalah sintaks Markdown lagi, panduan ini harus memberikan instruksi yang jelas dan lengkap untuk menyiapkan dan menjalankan proyek Anda. Jangan ragu untuk memberikan feedback jika ada masalah lebih lanjut!
