import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load data
day_data = pd.read_csv("data/day.csv")
hour_data = pd.read_csv("data/hour.csv")

day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

with st.sidebar:
    st.markdown(
        """
        <style>
            .profile-container {
                display: flex;
                align-items: center;
            }
            .githubImg {
                border-radius: 50%;
                width: 100px;
                height: 100px;
                margin-right: 10px;
            }
            .githubName {
                font-size: 16px;
                font-weight: bold;
                font-family: Arial, sans-serif;
            }
            .sidebar-text {
                font-size: 12px;
                font-weight: normal;
            }
        </style>
        <div class="profile-container">
            <img class="githubImg" src="https://avatars.githubusercontent.com/u/111998022?v=4" alt="Wahyu Pratama"/>
            <div class="githubName">Wahyu Pratama</div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.subheader("Task: Belajar Analisis Data dengan Python")
    st.markdown('<p class="sidebar-text">Email: wdicoding@gmail.com</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-text">ID Dicoding: wahyupratamaa</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-text">Dibuat: 8 Maret 2025</p>', unsafe_allow_html=True)

    st.markdown("[GitHub Project Link](https://github.com/whatyuupratama/Belajar_Analisis_Data_dengan_Python)", unsafe_allow_html=True)

    # Filter Tanggal
    min_date = day_data['dteday'].min()
    max_date = day_data['dteday'].max()
    selected_dates = st.date_input("Pilih Rentang Tanggal", [min_date, max_date], min_value=min_date, max_value=max_date)

# Filter data based on the selected date range
filtered_day_data = day_data[(day_data['dteday'] >= pd.to_datetime(selected_dates[0])) & (day_data['dteday'] <= pd.to_datetime(selected_dates[1]))]
filtered_hour_data = hour_data[(hour_data['dteday'] >= pd.to_datetime(selected_dates[0])) & (hour_data['dteday'] <= pd.to_datetime(selected_dates[1]))]

st.write(f"Menampilkan data antara {selected_dates[0]} dan {selected_dates[1]}")

# Visualisasi
st.title("Dashboard Analisis Sewa Sepeda dari Dataset Bike Sharing")
st.write("---")

# Pengaruh Cuaca terhadap Jumlah Sewa Sepeda
weather_map = {
    1: "Cerah",
    2: "Berawan",
    3: "Hujan"
}
filtered_day_data['weathersit'] = filtered_day_data['weathersit'].map(weather_map)

plt.figure(figsize=(10, 6))
sns.barplot(x=filtered_day_data['weathersit'], y=filtered_day_data['cnt'], palette='coolwarm')
plt.title('Pengaruh Cuaca terhadap Jumlah Sewa Sepeda')
plt.xlabel('Cuaca', labelpad=20)
plt.ylabel('Jumlah Sewa')
st.pyplot(plt)

st.write("---")

# Jumlah Sewa Sepeda Berdasarkan Hari dalam Seminggu
filtered_day_data['weekday'] = filtered_day_data['dteday'].dt.dayofweek
filtered_day_data['weekday'] = filtered_day_data['weekday'].map({
    0: 'Senin', 1: 'Selasa', 2: 'Rabu', 3: 'Kamis', 4: 'Jumat', 5: 'Sabtu', 6: 'Minggu'
})

plt.figure(figsize=(10, 6))
sns.barplot(x=filtered_day_data['weekday'], y=filtered_day_data['cnt'], palette='Set2')
plt.title('Jumlah Sewa Sepeda Berdasarkan Hari dalam Seminggu')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Jumlah Sewa')
st.pyplot(plt)

st.write("---")

# Tren Jumlah Sewa Sepeda Berdasarkan Jam dalam Sehari
def categorize_time(hour):
    if 5 <= hour < 10:
        return 'Pagi'
    elif 10 <= hour < 15:
        return 'Siang'
    elif 15 <= hour < 18:
        return 'Sore'
    else:
        return 'Malam'

filtered_hour_data['kategori_waktu'] = filtered_hour_data['hr'].apply(categorize_time)

plt.figure(figsize=(12, 6))
sns.lineplot(x=filtered_hour_data['kategori_waktu'], y=filtered_hour_data['cnt'], marker='o', color='green')
plt.title('Jumlah Sewa Sepeda Berdasarkan Waktu dalam Sehari')
plt.xlabel('Kategori Waktu')
plt.ylabel('Jumlah Sewa')
st.pyplot(plt)

st.write("---")

# Tren Musiman Jumlah Sewa Sepeda Berdasarkan Bulan
plt.figure(figsize=(12, 6))
sns.lineplot(x=filtered_hour_data['mnth'], y=filtered_hour_data['cnt'], marker='o', color='blue')
plt.title('Tren Musiman Jumlah Sewa Sepeda Berdasarkan Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Sewa')
plt.xticks(ticks=range(1, 13), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
st.pyplot(plt)

st.write("---")

# Kesimpulan
kesimpulan = """
Dari hasil analisis, kita dapat melihat bahwa faktor cuaca, suhu, dan hari dalam seminggu memiliki dampak yang signifikan 
terhadap jumlah sewa sepeda. Tren musiman juga menunjukkan pola-pola yang dapat dimanfaatkan untuk meningkatkan strategi 
pemasaran atau mengoptimalkan sistem peminjaman sepeda.
"""
st.subheader("Kesimpulan")
st.write(kesimpulan)
