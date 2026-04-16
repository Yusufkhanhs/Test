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
    try:
        genai.configure(api_key=api_key)
        
        # We use gemini-pro as it's the most stable for generateContent
        model = genai.GenerativeModel('gemini-pro')

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
                # Journalism Prompt
                prompt = f"Act as a Kannada journalist. Rewrite this news in formal Kannada: {content}"
                
                with st.spinner("Writing..."):
                    try:
                        # Attempt to generate content
                        response = model.generate_content(prompt)
                        st.markdown("### Result")
                        st.write(response.text)
                    except Exception as e:
                        # If gemini-pro fails, try the flash model name
                        st.info("Trying alternative model version...")
                        model_alt = genai.GenerativeModel('gemini-1.5-flash-latest')
                        response = model_alt.generate_content(prompt)
                        st.write(response.text)
            else:
                st.warning("Please provide content.")
    except Exception as e:
        st.error(f"Setup Error: {e}")
else:
    st.info("Please enter your API Key in the sidebar.")
