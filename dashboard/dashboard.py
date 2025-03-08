import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Atur gaya visualisasi
sns.set_theme(style="darkgrid", context="notebook")

#Load data dari file csv
def ambil_data():
    return pd.read_csv("dashboard/order_payments_customers_final.csv") 

df = ambil_data()

# Set konfigurasi halaman
st.set_page_config(page_title="E-Commerce Dashboard", page_icon="🛒", layout="wide")

# Sidebar dengan opsi navigasi
st.sidebar.title('Navigasi')
sidebar_option = st.sidebar.selectbox(
    'Pilih opsi untuk ditampilkan:',
    ['Total Jumlah Customer', 'Metode Pembayaran Paling Sering Digunakan', 'Grafik Pembayaran']
)

# Judul utama
st.title('🛒 E-Commerce Dashboard')

# Menampilkan konten sesuai pilihan di sidebar
if sidebar_option == 'Total Jumlah Customer':
    total_customers = df['customer_id'].nunique()  # Menghitung jumlah pelanggan unik
    st.subheader(f'📊 Total Jumlah Customer: {total_customers}')
    st.markdown("""
    Jumlah pelanggan unik yang menggunakan layanan e-commerce. Ini adalah total customer berdasarkan ID yang terdaftar.
    """)

    # Membuat bar chart dengan Matplotlib
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(['Total Customer'], [total_customers], color='skyblue', width=0.6)
    ax.set_ylabel('Jumlah Customer')
    ax.set_title('Total Jumlah Customer')

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)

elif sidebar_option == 'Metode Pembayaran Paling Sering Digunakan':
    # Cek apakah kolom 'payment_type' ada
    if 'payment_type' in df.columns:
        # Hapus NaN (jika ada) dan hitung frekuensi masing-masing metode pembayaran
        payment_method_counts = df['payment_type'].dropna().value_counts()
        
        if not payment_method_counts.empty:
            # Ambil metode pembayaran paling sering
            most_common_payment = payment_method_counts.idxmax()  # Metode pembayaran paling sering
            st.subheader(f'💳 Metode Pembayaran Paling Sering Digunakan: {most_common_payment}')
            st.markdown("""
            Metode pembayaran ini adalah yang paling sering dipilih oleh customer dalam melakukan transaksi e-commerce.
            """)
            st.bar_chart(payment_method_counts)  # Menampilkan grafik metode pembayaran
        else:
            st.warning("Tidak ada data metode pembayaran yang valid.")
    else:
        st.error("Kolom 'payment_type' tidak ditemukan dalam dataset!")


elif sidebar_option == 'Grafik Pembayaran':
    payment_method_counts = df['payment_type'].value_counts()
    st.subheader('📈 Grafik Metode Pembayaran')
    st.bar_chart(payment_method_counts)

# Menambahkan footer atau informasi lebih lanjut
st.markdown("""
---
Made with ❤️ by Dellanda
""")
