import streamlit as st
import pandas as pd
import tempfile

from parser import extract_text, extract_fields
from database import init_db, insert_receipt, fetch_all_receipts
from analytics import (
    preprocess_dataframe,
    get_top_vendors_by_frequency,
    get_top_vendors_by_spend,
    get_monthly_spend_trend,
    get_summary_stats
)

# 1. Setup Streamlit page
st.set_page_config(page_title="Receipt Analyzer", layout="wide")
st.title("📄 Receipt / Bill Parser & Analytics")

# 2. Connect to DB
conn = init_db()

# 3. Upload file
uploaded_file = st.file_uploader("Upload receipt (.txt, .pdf, .jpg, .png)", type=["txt", "pdf", "jpg", "png"])

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(uploaded_file.read())
        file_path = temp.name

    # Extract data
    text = extract_text(file_path)
    parsed = extract_fields(text)

    st.subheader("🔍 Parsed Receipt Data")
    st.json(parsed)

    if st.button("📥 Save to Database"):
        insert_receipt(conn, parsed)
        st.success("✅ Saved to database!")

# 4. Fetch all stored receipts
rows = fetch_all_receipts(conn)

if rows:
    df = pd.DataFrame(rows, columns=["id", "vendor", "date", "amount", "category"])
    df = preprocess_dataframe(df)

    st.subheader("Stored Receipts")
    st.dataframe(df)

    # 5. Show Summary Stats
    st.subheader("Spend Summary")
    st.write(get_summary_stats(df))

    # 6. Top Vendors
    st.subheader("Top Vendors (Frequency)")
    st.bar_chart(get_top_vendors_by_frequency(df))

    st.subheader("Top Vendors (Spend)")
    st.bar_chart(get_top_vendors_by_spend(df))

    # 7. Monthly Trend
    st.subheader("Monthly Spend Trend")
    monthly = get_monthly_spend_trend(df)
    if len(monthly) > 1:
        st.line_chart(monthly)
    else:
        st.info("Need ≥2 months of data to show trend.")
else:
    st.info("No receipts saved yet. Upload one above.")
