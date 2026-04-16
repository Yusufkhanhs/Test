import streamlit as st
from trafilatura import fetch_url, extract
import google.generativeai as genai

# Basic Page Setup
st.set_page_config(page_title="Kannada News Rewriter", layout="centered")

st.title("🗞️ Kannada Journalistic Rewriter")

# Sidebar Configuration
with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("Enter Gemini API Key", type="password")

# Main Application Logic
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        url = st.text_input("Paste English Article URL:")
        content_input = st.text_area("OR Paste English text:")

        if st.button("Rewrite in Kannada"):
            article_text = ""
            
            if url:
                with st.spinner("Extracting..."):
                    downloaded = fetch_url(url)
                    article_text = extract(downloaded)
            else:
                article_text = content_input

            if article_text:
                # This prompt ensures journalistic style and copyright safety
                prompt = f"""
                Act as a professional Kannada journalist. 
                Rewrite the following article in formal Kannada (Granthika style).
                1. Create a compelling news headline.
                2. Structure it as a news report (Inverted Pyramid style).
                3. Completely rephrase the content to ensure it is a new, original work in Kannada.
                
                Content to rewrite:
                {article_text}
                """
                
                with st.spinner("Writing..."):
                    response = model.generate_content(prompt)
                    st.markdown("---")
                    st.markdown("### ಪರಿಷ್ಕೃತ ಸುದ್ದಿ (Generated Article)")
                    st.write(response.text)
            else:
                st.warning("Please provide a URL or text content.")
                
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("👋 Please enter your API Key in the sidebar to start.")
