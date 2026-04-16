import streamlit as st
from trafilatura import fetch_url, extract
import google.generativeai as genai

# 1. Page Setup
st.set_page_config(page_title="Kannada News Rewriter", page_icon="🗞️")

st.title("🗞️ Kannada Journalistic Rewriter")
st.markdown("---")

# 2. Sidebar Configuration
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get a free key at aistudio.google.com")

# 3. Main Logic
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Input Options
    option = st.radio("Choose Input Method:", ("URL Link", "Manual Text"))
    
    text_to_process = ""

    if option == "URL Link":
        url = st.text_input("Enter English Article URL:")
        if url:
            with st.spinner("Fetching article..."):
                downloaded = fetch_url(url)
                text_to_process = extract(downloaded)
    else:
        text_to_process = st.text_area("Paste English Content here:", height=200)

    # 4. The Rewrite Button
    if st.button("Rewrite in Kannada"):
        if text_to_process:
            # Professional Journalistic Prompt
            prompt = f"""
            Act as a professional Kannada journalist. 
            Rewrite the following article in formal Kannada (Granthika style).
            - Create a news-style headline.
            - Summarize and restructure the content to avoid copyright issues.
            - Ensure the tone is neutral and informative.
            
            Article Content:
            {text_to_process}
            """
            
            with st.spinner("Writing..."):
                try:
                    response = model.generate_content(prompt)
                    st.subheader("Kannada News Version")
                    st.write(response.text)
                    st.success("Successfully rewritten!")
                except Exception as e:
                    st.error(f"AI Error: {e}")
        else:
            st.warning("Please provide content to rewrite.")
else:
    st.warning("Please enter your API Key in the sidebar to start.")
