import streamlit as st
from trafilatura import fetch_url, extract
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Kannada News Rewriter", page_icon="🗞️", layout="centered")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🗞️ Kannada Journalistic Rewriter")
st.subheader("Transform English articles into professional Kannada news.")

# Sidebar for Setup
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter Gemini API Key", type="password", help="Get a free key at aistudio.google.com")
    st.info("This app uses AI to rewrite content in a journalistic style to ensure transformative use and quality.")

# Logic
if api_key:
    try:
        genai.configure(api_key=api_key)
        # Using 1.5-flash for speed and local language support
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        tab1, tab2 = st.tabs(["Link (URL)", "Paste Text"])

        with tab1:
            url_input = st.text_input("Paste English Article URL:")
        
        with tab2:
            text_input = st.text_area("Paste English Content:", height=200)

        if st.button("Generate Kannada News Report"):
            article_text = ""
            
            # Extraction logic
            if url_input:
                with st.spinner("Extracting content from URL..."):
                    downloaded = fetch_url(url_input)
                    article_text = extract(downloaded)
            else:
                article_text = text_input

            if article_text:
                # The Journalism-Specific Prompt
                prompt = f"""
                Act as a senior editor for a leading Kannada daily newspaper like Prajavani or Udayavani. 
                Rewrite the following English content into a professional Kannada news article.
                
                Guidelines:
                1. Provide a bold, catchy headline in Kannada.
                2. Use the 'Inverted Pyramid' style (most critical info in the first paragraph).
                3. Maintain a formal, neutral, and journalistic tone (Standard Kannada/Granthika).
                4. Completely rephrase sentences to ensure 'Transformative Use' for copyright safety.
                5. Do not simply translate; rewrite the story for a Kannada-speaking audience.

                English Article Content:
                {article_text}
                """

                with st.spinner("Writing news in Kannada..."):
                    try:
                        response = model.generate_content(prompt)
                        st.markdown("---")
                        st.markdown("### 🖋️ ಪರಿಷ್ಕೃತ ಸುದ್ದಿ ವರದಿ (Generated Article)")
                        st.write(response.text)
                        
                        if url_input:
                            st.caption(f"ಮೂಲ ಕೃಪೆ (Original Source): {url_input}")
                            
                    except Exception as e:
                        st.error(f"AI Error: {e}")
            else:
                st.warning("Please provide either a URL or text content.")

    except Exception as e:
        st.error(f"Configuration Error: {e}")
else:
    st.info("👋 Please enter your Google Gemini API Key in the sidebar to begin.")
    st.markdown("""
    1. Go to [Google AI Studio](https://aistudio.google.com/).
    2. Click 'Get API Key'.
    3. Paste it in the sidebar.
    """)

# Footer
st.markdown("---")
st.caption("Built for Journalistic Transformation | Powered by Gemini AI")
