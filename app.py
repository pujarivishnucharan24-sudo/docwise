import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import pytesseract
from datetime import datetime
import re

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="DocWise AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 DocWise AI Dashboard")

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "receipts" not in st.session_state:
    st.session_state.receipts = []

# ---------------------------------------------------
# DASHBOARD METRICS
# ---------------------------------------------------

total_expenses = sum(
    r["Amount"] for r in st.session_state.receipts
)

receipt_count = len(st.session_state.receipts)

merchant_count = len(
    set(r["Merchant"] for r in st.session_state.receipts)
)

gst_saved = sum(
    r["GST"] for r in st.session_state.receipts
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Total Expenses", f"₹{total_expenses:.2f}")
c2.metric("🧾 Receipts", receipt_count)
c3.metric("🏪 Merchants", merchant_count)
c4.metric("📊 GST Saved", f"₹{gst_saved:.2f}")

st.divider()

# ---------------------------------------------------
# OCR FUNCTION
# ---------------------------------------------------

def process_receipt(uploaded_file):

    image = Image.open(uploaded_file)

    text = pytesseract.image_to_string(image)

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    merchant = lines[0] if lines else "Unknown Merchant"

    amount = 0

    amounts = re.findall(r'\d+\.\d{2}', text)

    if amounts:
        try:
            amount = max([float(x) for x in amounts])
        except:
            amount = 0

    return merchant, amount, text

# ---------------------------------------------------
# FILE UPLOAD + BUTTON
# ---------------------------------------------------

col1, col2 = st.columns([5, 1])

with col1:
    uploaded_file = st.file_uploader(
        "📤 Upload Receipt",
        type=["png", "jpg", "jpeg"]
    )

with col2:
    st.write("")
    st.write("")
    process_btn = st.button(
        "🚀 Process",
        use_container_width=True
    )

# ---------------------------------------------------
# PROCESS RECEIPT
# ---------------------------------------------------

if process_btn:

    if uploaded_file is None:

        st.warning("Please upload a receipt first.")

    else:

        with st.spinner("Processing receipt..."):

            merchant, amount, text = process_receipt(uploaded_file)

            now = datetime.now()

            gst = round(amount * 0.18, 2)

            receipt = {

                "Receipt ID":
                len(st.session_state.receipts) + 1,

                "File Name":
                uploaded_file.name,

                "Merchant":
                merchant,

                "Amount":
                amount,

                "GST":
                gst,

                "Date":
                now.strftime("%d-%m-%Y"),

                "Time":
                now.strftime("%H:%M:%S"),

                "Day":
                now.strftime("%A"),

                "Month":
                now.strftime("%B"),

                "Year":
                now.strftime("%Y"),

                "File Size (KB)":
                round(uploaded_file.size / 1024, 2),

                "Raw OCR Text":
                text
            }

            st.session_state.receipts.append(receipt)

            st.success("✅ Receipt processed and saved!")

            st.subheader("📄 OCR Extracted Text")

            st.text_area(
                "Receipt Text",
                text,
                height=250
            )

# ---------------------------------------------------
# DISPLAY DATA
# ---------------------------------------------------

if len(st.session_state.receipts) > 0:

    df = pd.DataFrame(st.session_state.receipts)

    st.divider()

    st.subheader("📊 Expenses Breakdown")

    fig = px.pie(
        df,
        names="Merchant",
        values="Amount",
        hole=0.4
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("🧾 Saved Receipts")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # ---------------------------------------------------
    # EXPORT BUTTONS
    # ---------------------------------------------------

    st.markdown("---")
    st.subheader("📥 Export Receipt Data")

    export_col1, export_col2 = st.columns(2)

    with export_col1:

        csv_data = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="⬇️ Download CSV",
            data=csv_data,
            file_name="docwise_receipts.csv",
            mime="text/csv",
            use_container_width=True
        )

    with export_col2:

        json_data = df.to_json(
            orient="records",
            indent=4
        )

        st.download_button(
            label="⬇️ Download JSON",
            data=json_data,
            file_name="docwise_receipts.json",
            mime="application/json",
            use_container_width=True
        )

else:

    st.info("No receipts processed yet.")
