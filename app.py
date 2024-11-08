import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import whisper
import re

# Load environment variables
load_dotenv()

# Configure Google Gemini Pro API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Whisper model for local video transcription
whisper_model = whisper.load_model("base")

# Prompt for Gemini API
prompt = """
You are a multi-language video summarizer. You will summarize the entire video based on the transcript 
and provide an important summary in bullet points within 350 words. Here's the transcript: 
"""

# Function to extract YouTube transcript
def extract_youtube_transcript(youtube_video_url, language_code="en"):
    try:
        video_id = extract_video_id(youtube_video_url)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
        return " ".join([i["text"] for i in transcript_text])
    except Exception as e:
        raise e

# Function to transcribe local video files
def transcribe_local_video(file_path):
    result = whisper_model.transcribe(file_path)
    return result['text']

# Function to generate summary using Google Gemini API
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Function to extract YouTube video ID
def extract_video_id(url):
    pattern = r"(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|shorts\/))([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        st.error("Invalid YouTube URL. Please try again.")
        return None

# Streamlit App Design
st.set_page_config(page_title="Multi-Language Video Transcript Summarizer", layout="wide")

# Theme selection: Light mode or Dark mode
mode = st.sidebar.radio("Toggle Theme", ("Light Mode", "Dark Mode"))

# CSS for Light Mode
# CSS for Light Mode
light_mode_css = """
   body {
    background-image: url('https://drive.google.com/file/d/1jfhCE7jr4xqCFapedf-6yhHb4i1oFgFD/view?usp=sharing');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}

    .main {
        background-color: transparent;
        color: #2C3E50;  # Dark blue-gray for text
    }
    h1 {
        color: #3498DB;  # Tech blue for headers
        text-align: center;
    }
    .stTextInput input {
        border: 2px solid #3498DB;  # Tech blue border
        padding: 10px;
        width: 100%;
        border-radius: 5px;
        background-color: rgba(255, 255, 255, 0.9);  # Slightly less transparent white background
        color: #2C3E50;  # Dark blue-gray for input text
    }
    .stButton button {
        background-color: #1ABC9C;  # Teal for buttons
        color: #ffffff;  # White button text
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #16A085;  # Darker teal on hover
    }
    .rating {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .star {
        font-size: 2em;
        color: #F1C40F;  # Yellow stars
        cursor: pointer;
    }
    .star:hover {
        color: #F39C12;  # Darker yellow on hover
    }
    .stSelectbox select {
        background-color: rgba(255, 255, 255, 0.9);  # Slightly less transparent background
        color: #2C3E50;  # Dark blue-gray text
        border: 2px solid #3498DB;  # Tech blue border
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
"""

# CSS for Dark Mode
# CSS for Dark Mode
# CSS for Dark Mode
dark_mode_css = """
    body {
        background-color: #20232A;
        color: #C0C0C0;
    }
    .main {
        background-color: #20232A;
        color: #C0C0C0;
    }
    h1 {
        color: #00ACC1;
        text-align: center;
    }
    .stTextInput label, .stSelectbox label {
        color: #00BFAE;  /* Light teal for labels */
    }
    .stTextInput input {
        border: 2px solid #00ACC1;
        padding: 10px;
        width: 100%;
        border-radius: 5px;
        background-color: #20232A;
        color: #C0C0C0;
    }
    .stTextInput input::placeholder {
        color: #A0A0A0;  /* Light gray for YouTube link placeholder */
        font-style: italic;
    }
    .stButton button {
        background-color: #00ACC1;
        color: #C0C0C0;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #00838F;
    }
    .rating {
        display: flex;
        justify-content: center;
        align-items: center;
        color: #00BFAE;  /* Light teal for "Select a rating:" text */
    }
    .star {
        font-size: 2em;
        color: #00BFAE;  /* Light teal for stars */
        cursor: pointer;
    }
    .star:hover {
        color: #009688;  /* Darker teal for hover effect */
    }
    .stSelectbox select {
        background-color: #20232A;
        color: #C0C0C0;
        border: 2px solid #00ACC1;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
"""
# Apply CSS based on the selected mode
if mode == "Light Mode":
    st.markdown(f'<style>{light_mode_css}</style>', unsafe_allow_html=True)
else:
    st.markdown(f'<style>{dark_mode_css}</style>', unsafe_allow_html=True)

# Header section
st.markdown("<h1>🎥 Multi-Language Video Transcript Summarizer 📋</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 18px;'>Convert YouTube or local video transcripts into detailed notes with AI-powered summarization.</p>", unsafe_allow_html=True)
st.write("---")

# Video source selection
video_source = st.selectbox("Select the video source:", ["YouTube", "Local Video"])

# Function to get YouTube thumbnail URL
def get_youtube_thumbnail_url(video_id):
    return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

# Generate summary for YouTube video
if video_source == "YouTube":
    with st.container():
        st.markdown(f"### <span style='color:#4CAF50;'>Enter the YouTube Video URL:</span>", unsafe_allow_html=True)
        youtube_link = st.text_input("Paste the YouTube video link here:", placeholder="e.g., https://www.youtube.com/watch?v=VIDEO_ID")

    # Language selection for YouTube transcript
    language_code = st.selectbox("Select transcript language:", ["en", "es", "fr", "de", "hi", "ja", "ko"])

    # Generate summary for YouTube video
    if youtube_link and st.button("Generate Summary for YouTube Video"):
        with st.spinner("Extracting transcript and generating summary..."):
            try:
                video_id = extract_video_id(youtube_link)
                
                # Display the YouTube thumbnail
                if video_id:
                    thumbnail_url = get_youtube_thumbnail_url(video_id)
                    st.image(thumbnail_url, caption="YouTube Video Thumbnail", use_column_width=True)

                transcript_text = extract_youtube_transcript(youtube_link, language_code)
                if transcript_text:
                    summary = generate_gemini_content(transcript_text, prompt)
                    st.markdown(f"<h2 style='color: #4CAF50;'>🔍 Detailed Notes:</h2>", unsafe_allow_html=True)
                    st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")

elif video_source == "Local Video":
    uploaded_file = st.file_uploader("Upload a local video file:", type=["mp4", "mkv", "avi"])

    if uploaded_file and st.button("Generate Summary for Local Video"):
        with st.spinner("Transcribing video and generating summary..."):
            try:
                transcript_text = transcribe_local_video(uploaded_file)
                if transcript_text:
                    summary = generate_gemini_content(transcript_text, prompt)
                    st.markdown(f"<h2 style='color: #4CAF50;'>🔍 Detailed Notes:</h2>", unsafe_allow_html=True)
                    st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")

# Star rating system
st.markdown(f"<h2 style='color: #4CAF50;'>⭐ Rate Us!</h2>", unsafe_allow_html=True)
rating = st.selectbox("Select a rating:", [5, 4, 3, 2, 1])
if st.button("Submit Rating"):
    st.success(f"Thank you for your rating of {rating} star{'s' if rating > 1 else ''}!")
