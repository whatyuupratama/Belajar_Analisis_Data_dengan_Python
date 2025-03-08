import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

day_data = pd.read_csv("data/day.csv")
hour_data = pd.read_csv("data/hour.csv")

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

    st.markdown("[GitHub Project Link](https://github.com/wahyupratamaa)", unsafe_allow_html=True)



   
st.title("Dashboard Analisis Sewa Sepeda dari Dataset Bike Sharing")
st.write("---")

st.subheader("pt1. : Bagaimana pengaruh cuaca dan hari dalam seminggu terhadap jumlah sepeda yang disewa")
st.write("---")

st.subheader("Pengaruh Cuaca terhadap Jumlah Sewa Sepeda")
plt.figure(figsize=(10, 6))
sns.boxplot(x=day_data['weathersit'], y=day_data['cnt'], hue=day_data['weathersit'], palette='coolwarm', legend=False)
plt.title('Pengaruh Cuaca terhadap Jumlah Sewa Sepeda')
plt.xlabel('Cuaca')
plt.ylabel('Jumlah Sewa')
st.pyplot(plt)

st.subheader("Jumlah Sewa Sepeda Berdasarkan Hari dalam Seminggu")
plt.figure(figsize=(10, 6))
sns.boxplot(x=day_data['weekday'], y=day_data['cnt'], hue=day_data['weekday'], palette='Set2', legend=False)
plt.title('Jumlah Sewa Sepeda Berdasarkan Hari dalam Seminggu')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Jumlah Sewa')
st.pyplot(plt)

st.write("---")

st.subheader("pt2. : Apakah ada tren musiman atau pola berdasarkan waktu dalam sehari yang mempengaruhi jumlah sewa sepeda")
st.write("---")

st.subheader("Tren Jumlah Sewa Sepeda Berdasarkan Jam dalam Sehari")
plt.figure(figsize=(12, 6))
sns.lineplot(x=hour_data['hr'], y=hour_data['cnt'], marker='o', color='green')
plt.title('Jumlah Sewa Sepeda Berdasarkan Waktu dalam Sehari')
plt.xlabel('Jam dalam Sehari')
plt.ylabel('Jumlah Sewa')
plt.xticks(rotation=45)
st.pyplot(plt)

st.write("---")

st.subheader("Tren Musiman Jumlah Sewa Sepeda Berdasarkan Bulan")
plt.figure(figsize=(12, 6))
sns.lineplot(x=hour_data['mnth'], y=hour_data['cnt'], marker='o', color='blue')
plt.title('Tren Musiman Jumlah Sewa Sepeda Berdasarkan Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Sewa')
plt.xticks(ticks=range(1, 13), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
st.pyplot(plt)

st.write("---")

kesimpulan = """
Dari hasil analisis, kita dapat melihat bahwa faktor cuaca, suhu, dan hari dalam seminggu memiliki dampak yang signifikan 
terhadap jumlah sewa sepeda. Tren musiman juga menunjukkan pola-pola yang dapat dimanfaatkan untuk meningkatkan strategi 
pemasaran atau mengoptimalkan sistem peminjaman sepeda.
"""
st.subheader("Kesimpulan")
st.write(kesimpulan)
