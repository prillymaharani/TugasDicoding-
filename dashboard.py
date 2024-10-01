import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul Dashboard
st.title("Dashboard Analisis Data Penyewaan Sepeda")

# Mengimpor Data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Menampilkan Statistik Deskriptif
st.header("Statistik Deskriptif")
st.subheader("Data Harian")
st.write(day_df.describe())

st.subheader("Data Jam")
st.write(hour_df.describe())

# Visualisasi Distribusi Suhu
st.header("Distribusi Suhu (Celsius)")
fig, ax = plt.subplots()
sns.histplot(day_df['temp'], bins=30, kde=True, ax=ax)
ax.set_title('Distribusi Suhu (Celsius)')
ax.set_xlabel('Suhu (Celsius)')
ax.set_ylabel('Frekuensi')
st.pyplot(fig)

# Analisis Korelasi
st.header("Matriks Korelasi")
numerical_columns = day_df.select_dtypes(include=['number']).columns
correlation_matrix = day_df[numerical_columns].corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, ax=ax)
ax.set_title('Matriks Korelasi (Day Data)')
st.pyplot(fig)

# Rata-rata Penyewaan Berdasarkan Jam
st.header("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
hourly_rentals = hour_df.groupby('hr')['cnt'].mean()
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=hourly_rentals)
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Rata-rata Penyewaan')
plt.xticks(range(0, 24))
st.pyplot(fig)

# Rata-rata Penyewaan Berdasarkan Hari dalam Seminggu
st.header("Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
weekly_rentals = day_df.groupby('weekday')['cnt'].mean()
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=weekly_rentals.index, y=weekly_rentals.values, ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Rata-rata Penyewaan')
plt.xticks(ticks=range(7), labels=['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
st.pyplot(fig)

# Insight dan Kesimpulan
st.header("Insight dan Kesimpulan")
st.write("""
1. **Faktor yang Mempengaruhi Penyewaan**: Suhu (temp) dan cuaca memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda. Semakin tinggi suhu, semakin banyak penyewaan yang terjadi.
2. **Pola Penyewaan**: Penyewaan sepeda lebih tinggi pada jam 8 pagi dan 5 sore, serta lebih banyak terjadi pada hari kerja dibandingkan akhir pekan.
""")
