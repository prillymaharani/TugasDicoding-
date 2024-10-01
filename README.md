# Proyek Analisis Data Penyewaan Sepeda

Proyek ini bertujuan untuk melakukan analisis data penyewaan sepeda menggunakan berbagai library Python. Dalam proyek ini, kami telah membuat dashboard interaktif menggunakan Streamlit untuk menyampaikan hasil analisis.

## 1. Pengaturan Lingkungan
Python versi  3.11.9

### 1.1. Membuat Virtual Environment (Opsional)
python -m venv env

# Mengaktifkan virtual environment
# Windows
env\Scripts\activate

## 2. Menjalankan Dependensi 
import os

# Isi dari file requirements.txt
requirements_content = """pandas
numpy
matplotlib
seaborn
scikit-learn
folium
streamlit
"""

# Path untuk menyimpan requirements.txt
path = ("requirements.txt")

# Membuat direktori jika belum ada
os.makedirs(os.path.dirname(path), exist_ok=True)

# Menyimpan berkas requirements.txt
with open(path, "w") as file:
    file.write(requirements_content)

print(f"File requirements.txt berhasil disimpan di {path}")
import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
import sklearn
import streamlit

# Menampilkan versi masing-masing library
print(f"pandas: {pd._version_}")
print(f"numpy: {np._version_}")
print(f"matplotlib: {matplotlib._version_}")
print(f"seaborn: {sns._version_}")
print(f"scikit-learn: {sklearn._version_}")
print(f"streamlit: {streamlit._version_}")

### Run steamlit app
open cmd
cd "C:\Study Independent\Submission(New)\dashboard"
streamlit run dashboard.py

