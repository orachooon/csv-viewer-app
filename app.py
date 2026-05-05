import streamlit as st
import pandas as pd

st.title("📊 CSV Viewer")
st.write("อัปโหลดไฟล์ CSV เพื่อดูข้อมูล")

uploaded_file = st.file_uploader("เลือกไฟล์ CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success(f"✅ โหลดข้อมูลสำเร็จ: {df.shape[0]} แถว, {df.shape[1]} คอลัมน์")

    st.subheader("👀 ตัวอย่างข้อมูล")
    st.dataframe(df)

    st.subheader("📈 สถิติเบื้องต้น")
    st.write(df.describe())

    st.subheader("🔢 ประเภทข้อมูลแต่ละคอลัมน์")
    st.write(df.dtypes)
