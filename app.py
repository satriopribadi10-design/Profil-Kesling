import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Profil Kesehatan Lingkungan Kabupaten Barito Timur 2026",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
    <style>
    .main-header {
        font-size: 24px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    file_path = "Propil Kesling 2026.xlsx"
    sheets_data = {}
    sheets_data["Sarana Air Minum"] = pd.read_excel(file_path, sheet_name="79 ", header=None)
    sheets_data["Fasilitas Sanitasi (Jamban Sehat)"] = pd.read_excel(file_path, sheet_name="80", header=None)
    sheets_data["Sanitasi Total Berbasis Masyarakat"] = pd.read_excel(file_path, sheet_name="81", header=None)
    sheets_data["Pengawasan TFU"] = pd.read_excel(file_path, sheet_name="82", header=None)
    sheets_data["Tempat Pengelolaan Pangan (TPP)"] = pd.read_excel(file_path, sheet_name="83", header=None)
    return sheets_data

try:
    sheets_data = load_data()
except Exception as e:
    st.error(f"Gagal memuat file Excel 'Propil Kesling 2026.xlsx': {e}")
    st.stop()

st.sidebar.title("📊 Navigasi Profil Kesling")
st.sidebar.markdown("---")
selected_menu = st.sidebar.radio("Pilih Menu Tabel:", list(sheets_data.keys()))

st.sidebar.markdown("---")
st.sidebar.info("💡 **Kabupaten Barito Timur**\nProfil Kesehatan Lingkungan Tahun 2026")

st.markdown(f'<div class="main-header">📋 {selected_menu}</div>', unsafe_allow_html=True)

raw_df = sheets_data[selected_menu]
st.subheader("Data Detail per Puskesmas & Kecamatan")
st.dataframe(raw_df, use_container_width=True, height=500)

csv = raw_df.to_csv(index=False, header=False)
st.download_button(
    label="📥 Unduh Data Tabel Ini (CSV)",
    data=csv,
    file_name=f"{selected_menu.replace(' ', '_')}.csv",
    mime="text/csv",
)
