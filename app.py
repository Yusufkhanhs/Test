import streamlit as st
from trafilatura import fetch_url, extract
import google.generativeai as genai

# Basic Page Config
st.set_page_config(page_title="Kannada News Rewriter", layout="centered")

st.title("🗞️ Kannada Journalistic Rewriter")

# Sidebar
with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("Enter Gemini API Key", type="password")

# Main Logic
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
                # This prompt ensures journalistic style and transformative rewrite
                prompt = f"""
                Rewrite this as a professional Kannada news journalist.
                1. Use a formal Kannada headline.
                2. Structure as a news report (most important facts first).
                3. Completely rephrase the content to ensure it is a new, original work in Kannada.
                Content to rewrite: {article_text}
                """
                
                with st.spinner("Rewriting..."):
                    response = model.generate_content(prompt)
                    st.markdown("### Result")
                    st.write(response.text)
            else:
                st.warning("Please provide a URL or text.")
                
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please enter your API Key in the sidebar.")
