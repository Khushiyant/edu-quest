import openai
import streamlit as st
import wikipedia as wiki

openai.api_key = st.secrets["OPENAI_KEY"]

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


def generate_query(query):

    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=query,
        temperature=0.3,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    st.text(response.choices[0].text)


def main():

    st.header("Notes and Questions")
    text_input = st.text_input("Enter a title or topic")

    if text_input:
        option = st.selectbox(
            'What are the actions you want to perform?',
            ['Notes', 'Questions'])

        summary = None

        try:
            summary = wiki.summary(text_input)
        except BaseException:
            summary = generate_query(
                f"Generate summary on the topic: {text_input}")
            
        if option == 'Notes':
            response = summary
            st.write(response)
        elif option == 'Questions':
            response = generate_query(
                f"Generate list of questions based the given summary: {summary}")
            st.write(response)


if __name__ == '__main__':
    main()
