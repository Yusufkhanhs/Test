import streamlit as st
from trafilatura import fetch_url, extract
import google.generativeai as genai

# Setup
st.set_page_config(page_title="Kannada News Rewriter", layout="wide")
st.title("🗞️ Kannada Journalistic Rewriter")

# Sidebar for API Key (Get a free one at aistudio.google.com)
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    url = st.text_input("Paste English Article URL here:")
    content_input = st.text_area("OR Paste English text here:")

    if st.button("Rewrite in Kannada"):
        text_to_process = ""
        
        if url:
            downloaded = fetch_url(url)
            text_to_process = extract(downloaded)
        else:
            text_to_process = content_input

        if text_to_process:
            # The "Journalistic" Prompt
            prompt = f"""
            Act as a professional Kannada news journalist. 
            Rewrite the following English content into a formal, engaging journalistic report in Kannada.
            - Use a catchy headline.
            - Follow an 'Inverted Pyramid' style (most important info first).
            - Use formal Kannada (not colloquial).
            - Ensure it is a fresh rewrite to avoid copyright infringement.
            
            English Content: {text_to_process}
            """
            
            with st.spinner("Translating and Rewriting..."):
                response = model.generate_content(prompt)
                st.subheader("Generated Kannada News Article")
                st.write(response.text)
                if url:
                    st.info(f"Source: {url}")
        else:
            st.error("Please provide a URL or text content.")
else:
    st.warning("Please enter your Google Gemini API Key in the sidebar to start.")
