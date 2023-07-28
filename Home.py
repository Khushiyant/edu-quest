import streamlit as st
import streamlit.components.v1 as components


OpenAI_Key = st.secrets["OPENAI_KEY"]

st.set_page_config(
    page_title="Wissen",
    page_icon="https://static.wixstatic.com/media/a031de_cf6b54385e4c454bad311b0ef709f7be~mv2.png/v1/fit/w_2500,h_1330,al_c/a031de_cf6b54385e4c454bad311b0ef709f7be~mv2.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.image("https://static.wixstatic.com/media/a031de_cf6b54385e4c454bad311b0ef709f7be~mv2.png/v1/fit/w_2500,h_1330,al_c/a031de_cf6b54385e4c454bad311b0ef709f7be~mv2.png", width=400)

st.markdown("""
#### Welcome to Wissen - a 5 in 1 education multitool for students.

**Text Summarizer**: Use our Text Summarizer to efficiently generate concise summaries from PDFs, articles, or input text. Save time and get the main points without reading lengthy content.

**Video Summarizer**: With the Video Summarizer, simply paste a YouTube video URL, and we'll provide you with a summary that includes the essential keywords used. No need to watch the entire video to grasp its content.

**Notes and Questions** : Input any topic, and our tool will generate comprehensive notes or questions related to that subject. Enhance your learning experience with organized and structured content.

**Semantic Search**: Upload a text file and benefit from our advanced Semantic Search feature. Easily find relevant information based on keywords, making research faster and more efficient.

**Scripture Teacher** : Interact with our scripture teacher which enlighten us on topic of various religious scriptures.
""")
