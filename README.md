# Multi-Language Video Transcript Summarizer

Welcome to the **Multi-Language Video Transcript Summarizer**! This application allows users to extract transcripts from YouTube or local videos and convert them into concise summaries using the Google Gemini AI API. With support for multiple languages and both light and dark themes, the app is designed to be user-friendly and visually appealing.

## Features

- **YouTube Transcript Summarization**: Extract transcripts from YouTube videos in various languages and generate concise summaries.
- **Local Video Transcription**: Upload local video files for transcription and summarization.
- **Multi-Language Support**: Choose from several language options to customize the transcript extraction.
- **Customizable Themes**: Toggle between Light and Dark modes for a personalized user experience.
- **Star Rating System**: Provide feedback with a 1-5 star rating system.

## Technologies Used

- **Python**
- **Streamlit**: For building the web app interface.
- **Google Gemini AI API**: Used to generate summaries from transcripts.
- **Whisper by OpenAI**: For local video transcription.
- **YouTube Transcript API**: To fetch transcripts from YouTube videos.
- **dotenv**: To load environment variables.

## Installation and Setup

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your_username/multi-language-video-summarizer.git
    cd multi-language-video-summarizer
    ```

2. **Install Required Libraries**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Google Gemini API key:
     ```plaintext
     GOOGLE_API_KEY=your_google_api_key_here
     ```

4. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

## How to Use

1. **Select the Video Source**: Choose between "YouTube" or "Local Video" as the video source.
2. **Extract Transcript**:
   - **For YouTube**: Enter the YouTube video link and select the desired transcript language.
   - **For Local Video**: Upload a video file (supported formats: `.mp4`, `.mkv`, `.avi`).
3. **Generate Summary**: Click the button to extract the transcript and summarize it.
4. **Rate the App**: After using the app, rate your experience to help improve the tool.

## Project Structure

```plaintext
├── app.py                # Main application file
├── requirements.txt      # Required Python libraries
└── .env                  # Environment variables file
```

## Customizing Themes

The app includes custom CSS for Light and Dark modes. Adjust the color codes in `app.py` if you want to personalize the themes.

## License

This project is licensed under the MIT License.

---

Happy Summarizing!
