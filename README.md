# BasicTranscriptor
Basic Streamlit interface for a whisper based transcriptor

## Create the Conda environment:
### Directly using requirements.txt
conda create -n VOICE python=3.11

pip install -r requirements.txt
### Using the conda
conda env create -f VOICE.yml

## Execute the app:
streamlit run .\app_transcript.py
