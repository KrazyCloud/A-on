import streamlit as st
from files.cleaning_text import clean_transcript
from files.extract import extract_video_id
from files.generator import *
from files.transcript import transcript_generator
from config.query_api import get_answers

# Function to get a limited number of words from a sentence
def get_limited_words(sentence, limit=30):
    words = sentence.split()
    limited_words = ' '.join(words[:limit])
    return limited_words

def main():
    # titles and head
    st.title("_:red[Youtube]_ Transcript Chatbot")
    st.markdown("Welcome to the chat! Type your messages below.")
    st.header("",divider="gray")

    video_url = st.text_input("Enter YouTube Video URL")
    if video_url:
        video_id = extract_video_id(video_url)
        if video_id:
            transcript = transcript_generator(video_id)
            cleaned_transcript = clean_transcript(transcript)

            user_input = st.text_input("Ask something")

            if user_input:
                
                answers = get_answers(user_input, cleaned_transcript)
                combined_answer = " ".join(answers)
                limited_response = get_limited_words(combined_answer, 50)
                st.text_area("Chatbot's Response", limited_response)
            else:
                st.write("Please ask something")
        else:
            st.write("Invalid YouTube Video URL")


if __name__ == "__main__":
    main()