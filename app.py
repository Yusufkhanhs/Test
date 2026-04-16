import streamlit as st
import google.generativeai as genai
from trafilatura import fetch_url, extract

st.set_page_config(page_title="Kannada News Rewriter")
st.title("🗞️ Kannada Journalistic Rewriter")

# Sidebar
with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    url = st.text_input("Article URL:")
    text_input = st.text_area("Or Paste English Text:")

    if st.button("Rewrite in Kannada"):
        content = ""
        if url:
            with st.spinner("Extracting..."):
                downloaded = fetch_url(url)
                content = extract(downloaded)
        else:
            content = text_input

        if content:
            # This prompt ensures the rewrite is 'Transformative' for copyright safety
            prompt = f"Rewrite this English news as a professional Kannada journalist. Use formal Kannada: {content}"
            
            with st.spinner("Writing..."):
                try:
                    response = model.generate_content(prompt)
                    st.markdown("### Result")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"AI Error: {e}")
        else:
            st.warning("Please provide content.")
else:
    st.info("Please enter your API Key in the sidebar.")
