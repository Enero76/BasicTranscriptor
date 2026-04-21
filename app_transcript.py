import streamlit as st
import whisper
import tempfile

st.title("Whisper Transcription")

model = whisper.load_model("base")

audio_file = st.file_uploader("Upload an audio file to transcribe", type=["wav", "mp3", "m4a"])

if audio_file:
    st.audio(audio_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    if st.button("Transcribe"):
        result = model.transcribe(tmp_path)
        st.text_area("Text", result["text"], height=200)
