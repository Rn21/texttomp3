import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
import io

# --- Page Configuration ---
st.set_page_config(
    page_title="Text-to-Audio with Pauses",
    page_icon="🔊",
    layout="centered",  # 'centered' is better for mobile
    initial_sidebar_state="auto",
)

# --- App Title and Description ---
st.title("📜 Text-to-Audio Converter")
st.markdown(
    "Upload a text file, and this app will generate an audio version with "
    "customizable pauses between each line. Perfect for speeches, scripts, or study notes!"
)

# --- Core Functions ---

def text_to_audio_with_pauses(text, pause_duration_ms):
    """
    Converts a block of text to an audio file, adding a specified pause after each line.

    Args:
        text (str): The input text.
        pause_duration_ms (int): The duration of the pause in milliseconds.

    Returns:
        io.BytesIO: A BytesIO object containing the generated MP3 audio data.
    """
    # Split text into lines and filter out any empty lines
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]

    if not lines:
        st.warning("The uploaded text file is empty or contains no valid lines.")
        return None

    # Create the silent segment for the pause
    pause = AudioSegment.silent(duration=pause_duration_ms)
    
    # Initialize a variable to hold the combined audio
    combined_audio = AudioSegment.empty()

    # Process each line and add it to the combined audio
    st.info(f"Processing {len(lines)} lines of text...")
    progress_bar = st.progress(0)

    try:
        for i, line in enumerate(lines):
            # Use gTTS to convert the current line of text to speech
            tts = gTTS(text=line, lang='en')
            
            # Save the speech to an in-memory file
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            
            # Load the speech segment from the in-memory file
            speech_segment = AudioSegment.from_mp3(mp3_fp)
            
            # Append the speech and the pause
            combined_audio += speech_segment
            if i < len(lines) - 1:  # Don't add a pause after the last line
                combined_audio += pause
            
            # Update the progress bar
            progress_bar.progress((i + 1) / len(lines))

        # Export the final combined audio to an in-memory file
        output_fp = io.BytesIO()
        combined_audio.export(output_fp, format="mp3")
        output_fp.seek(0)
        
        st.success("Audio generated successfully!")
        return output_fp

    except Exception as e:
        st.error(f"An error occurred during audio generation: {e}")
        st.error(
            "This could be due to a network issue or an invalid character in the text. "
            "Please check your internet connection and the text file."
        )
        return None

# --- UI Components ---

# File Uploader
st.header("1. Upload Your Text File")
uploaded_file = st.file_uploader(
    "Choose a .txt file",
    type="txt",
    help="Upload the text file you want to convert to audio."
)

if uploaded_file is not None:
    # To read file as string:
    text_data = uploaded_file.getvalue().decode("utf-8")
    
    st.text_area("File Content Preview", text_data, height=150)

    st.header("2. Set Your Pause Duration")
    pause_duration = st.slider(
        "Pause between lines (in seconds)",
        min_value=0.5,
        max_value=5.0,
        value=1.5,  # Default to 1.5 seconds
        step=0.1,
        help="This is the length of the silence added after each line of text."
    )
    
    st.header("3. Generate and Play Audio")
    if st.button("Generate Audio 🎧", type="primary"):
        with st.spinner("Generating audio... Please wait."):
            # Convert pause from seconds to milliseconds for pydub
            pause_ms = int(pause_duration * 1000)
            
            # Call the conversion function
            audio_bytes_io = text_to_audio_with_pauses(text_data, pause_ms)
            
            # Store the result in session state to persist it
            if audio_bytes_io:
                st.session_state.audio_data = audio_bytes_io.getvalue()
            else:
                st.session_state.audio_data = None


# Display audio player and download button if audio has been generated
if 'audio_data' in st.session_state and st.session_state.audio_data:
    st.audio(st.session_state.audio_data, format='audio/mp3')
    
    # Get the original filename to create a new audio filename
    original_filename = uploaded_file.name.rsplit('.', 1)[0]
    audio_filename = f"{original_filename}_audio.mp3"

    st.download_button(
        label="Download Audio File (.mp3)",
        data=st.session_state.audio_data,
        file_name=audio_filename,
        mime="audio/mp3",
    )

# --- Footer ---
st.markdown("---")
st.markdown("Made by Raam Nayakar using [Streamlit](https://streamlit.io), [gTTS](https://gtts.readthedocs.io), and [Pydub](https://github.com/jiaaro/pydub).")