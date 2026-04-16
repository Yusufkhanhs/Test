import streamlit as st
import google.generativeai as genai
from trafilatura import fetch_url, extract

# 1. Embedded API Key
API_KEY = "AIzaSyDSrVdXhy5nSl_CIVcL4fiQb8pJv793c6E"

st.set_page_config(page_title="Kannada News Rewriter", page_icon="🗞️")
st.title("🗞️ Kannada Journalistic Rewriter")

# Configure the SDK with your key
try:
    genai.configure(api_key=API_KEY)
    
    # AUTO-SELECT MODEL: This finds what the key actually supports
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    if not available_models:
        st.error("No models found. Please check if the API key is active.")
    else:
        # Select the best available model
        selected_model_name = available_models[0]
        for m in available_models:
            if '1.5-flash' in m:
                selected_model_name = m
                break
        
        st.caption(f"Status: Connected | Model: {selected_model_name}")
        model = genai.GenerativeModel(selected_model_name)

        # UI Input
        url = st.text_input("Paste English Article URL:")
        text_input = st.text_area("Or Paste English Text:")

        if st.button("Rewrite in Kannada"):
            content = ""
            if url:
                with st.spinner("Extracting news content..."):
                    downloaded = fetch_url(url)
                    content = extract(downloaded)
            else:
                content = text_input

            if content:
                # The Journalism Prompt
                prompt = f"""
                Act as a professional Kannada news editor. 
                Rewrite the following English article into formal, high-quality Kannada.
                - Create a strong news headline.
                - Use a professional journalistic tone.
                - Ensure the content is completely rephrased to be a new, original work.
                
                Article content:
                {content}
                """
                
                with st.spinner("Generating Kannada Article..."):
                    try:
                        response = model.generate_content(prompt)
                        st.markdown("---")
                        st.subheader("ಪರಿಷ್ಕೃತ ಕನ್ನಡ ಸುದ್ದಿ ವರದಿ")
                        st.write(response.text)
                        st.success("Rewrite Complete!")
                    except Exception as e:
                        st.error(f"Generation Error: {e}")
            else:
                st.warning("Please provide a URL or paste text first.")

except Exception as e:
    st.error(f"Connection Error: {e}")

# Footer
st.markdown("---")
st.caption("Free Journalistic Rewriter | Powered by Gemini")
