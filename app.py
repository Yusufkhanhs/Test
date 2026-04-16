import streamlit as st
import google.generativeai as genai
from trafilatura import fetch_url, extract
import time

# Embedded Key (Use yours here)
API_KEY = "AIzaSyDSrVdXhy5nSl_CIVcL4fiQb8pJv793c6E"

st.set_page_config(page_title="Free Kannada News AI", page_icon="📰")
st.title("📰 Free Kannada News Generator")

genai.configure(api_key=API_KEY)
# Flash is the best for FREE use as it has higher limits than 'Pro'
model = genai.GenerativeModel('gemini-1.5-flash')

url = st.text_input("Enter News URL:")
text_data = st.text_area("Or Paste News Text:")

if st.button("Generate Kannada News"):
    content = ""
    if url:
        with st.spinner("Reading article..."):
            content = extract(fetch_url(url))
    else:
        content = text_data

    if content:
        # Prompt designed to be fast and journalistic
        prompt = f"Rewrite this as a Kannada news report with a headline: {content}"
        
        try:
            with st.spinner("AI is thinking..."):
                response = model.generate_content(prompt)
                st.markdown("### ಪರಿಷ್ಕೃತ ಸುದ್ದಿ (Kannada News)")
                st.write(response.text)
        except Exception as e:
            if "429" in str(e):
                st.error("Too many requests! Please wait 30 seconds. The Free Tier allows 15 requests per minute.")
                time.sleep(30) # Self-imposed cooling
            else:
                st.error(f"Error: {e}")
    else:
        st.warning("Input some content first!")
