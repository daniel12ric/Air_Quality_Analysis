import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Setup halaman ---
st.set_page_config(page_title="Dashboard Kualitas Udara", layout="wide")

# --- Judul utama ---
st.title("🌫️ Dashboard Analisis Kualitas Udara (PM2.5)")

# --- Load data ---
@st.cache_data
def load_data():
    return pd.read_csv("air_quality.csv")

df = load_data()

# --- Sidebar filter ---
with st.sidebar:
    st.header("🔧 Filter Data")
    year = st.selectbox("Pilih Tahun", sorted(df['year'].unique()))
    station = st.selectbox("Pilih Stasiun", sorted(df['station'].unique()))

# --- Filter data sesuai pilihan ---
filtered_df = df[(df['year'] == year) & (df['station'] == station)]

# --- Tampilan tabel awal ---
st.markdown(f"### 🧾 Data PM2.5 di Stasiun `{station}` Tahun `{year}`")
st.dataframe(filtered_df[['year','month','day','PM2.5']].dropna().head(10), use_container_width=True)

# --- Chart 1: Trend PM2.5 per Bulan ---
st.markdown("## 📈 Rata-rata PM2.5 per Bulan")
avg_monthly = filtered_df.groupby('month')['PM2.5'].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(8,4))
sns.barplot(data=avg_monthly, x='month', y='PM2.5', palette='magma', ax=ax1)
ax1.set_title(f"Rata-rata PM2.5 per Bulan di {station} ({year})")
ax1.set_xlabel("Bulan")
ax1.set_ylabel("PM2.5")
st.pyplot(fig1)

# --- Chart 2: Korelasi antar variabel ---
st.markdown("## 🔍 Korelasi Antar Variabel Cuaca & Polusi")
with st.expander("Lihat Heatmap Korelasi"):
    corr = filtered_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()
    fig2, ax2 = plt.subplots(figsize=(10,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax2)
    ax2.set_title("Heatmap Korelasi Variabel")
    st.pyplot(fig2)

# --- Pertanyaan 2: Lokasi dengan PM2.5 tertinggi & terendah ---
st.markdown("## 📍 Lokasi dengan Tingkat PM2.5 Tertinggi dan Terendah")

pm25_by_station = df.groupby('station')['PM2.5'].mean().sort_values(ascending=False).reset_index()

fig3, ax3 = plt.subplots(figsize=(10,5))
sns.barplot(data=pm25_by_station, x='station', y='PM2.5', palette='coolwarm', ax=ax3)
ax3.set_title("Rata-rata PM2.5 per Lokasi Stasiun")
ax3.set_xlabel("Stasiun")
ax3.set_ylabel("Rata-rata PM2.5")
ax3.tick_params(axis='x', rotation=45)
st.pyplot(fig3)

highest = pm25_by_station.iloc[0]
lowest = pm25_by_station.iloc[-1]

col1, col2 = st.columns(2)
with col1:
    st.success(f"📌 Tertinggi: `{highest['station']}` — **{highest['PM2.5']:.2f}**")
with col2:
    st.warning(f"📌 Terendah: `{lowest['station']}` — **{lowest['PM2.5']:.2f}**")

# --- Insight & interpretasi ---
st.markdown("## 💡 Insight Penting")
st.info(f"""
- PM2.5 di stasiun **{station}** cenderung meningkat pada bulan-bulan musim dingin (Desember–Februari).
- Korelasi menunjukkan bahwa **PM2.5** sangat berkorelasi dengan **PM10** dan cukup dipengaruhi oleh **suhu (TEMP)** dan **kecepatan angin (WSPM)**.
- Stasiun dengan rata-rata PM2.5 tertinggi adalah **{highest['station']}**, sementara terendah adalah **{lowest['station']}**.
""")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 | Dashboard Analisis Udara Project - Dibuat dengan ❤️ oleh Daniel Darren Richardo")
