from docarray import Document, DocumentArray
import streamlit as st
import openai
import re
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


def semantic(txt_file):
    if txt_file is not None:
        text = txt_file.read()
        text = text.decode("utf-8")
        documents = DocumentArray([Document(text=text)])
        query = st.text_input("Ask me anything")
        response = openai.Engine("gpt-3.5-turbo").search(documents, query)
        return (response[0].matches, response[0].scores)


def main():
    st.header("Semantic Document Search")
    txt_file = st.file_uploader("Upload a text file", type=["txt"])

    result = semantic(txt_file)
    if txt_file:
        length = len(result[0])
        for i in range(length):
            value = str(result[1][i])
            match = re.search(r"'value':\s*([\d.]+)", value)
            if match:
                value = float(match.group(1))
                st.write(result[0][i] + f" Score: `{value}`")


if __name__ == '__main__':
    main()
