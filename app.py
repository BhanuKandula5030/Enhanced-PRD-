
import streamlit as st
import os
from utils import summarize_prd, generate_uat_cases

st.set_page_config(page_title="PRD Summarizer & UAT Generator", layout="centered")

st.title("📄 PRD Summarizer & 🧠 GPT-style UAT Generator")
st.markdown("Upload your PRD and get a summary plus user acceptance test cases like a Product Owner would write.")

api_key = st.text_input("🔐 Enter your OpenAI API Key", type="password")

uploaded_file = st.file_uploader("Upload PRD (.txt format)", type=["txt"])

if uploaded_file and api_key:
    content = uploaded_file.read().decode("utf-8")

    st.subheader("📌 Summary")
    summary = summarize_prd(content, api_key)
    st.text_area("Summary", summary, height=200)

    st.subheader("✅ UAT Test Cases")
    uat_cases = generate_uat_cases(content, api_key)
    st.text_area("UAT Test Cases", uat_cases, height=300)

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    with open("outputs/uat_cases.txt", "w", encoding="utf-8") as f:
        f.write(uat_cases)

    st.download_button("📥 Download Summary", summary, file_name="summary.txt")
    st.download_button("📥 Download UAT Cases", uat_cases, file_name="uat_cases.txt")
