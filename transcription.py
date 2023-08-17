import os
import glob
import time
from faster_whisper import WhisperModel

model_size = "medium" # You can choose between tiny, base, small, medium and large. The larger the model you choose, the better the quality, but you'll need more performance (by default, the medium model works on just about all computers, but can be a little slow).  
output_transcript_file = "transcript.txt"
audio_file_pattern = "audio_output_file_*.flac"

model = WhisperModel(model_size, device="cpu", compute_type="int8")

def transcribe_audio(audio_file):
    segments, _ = model.transcribe(audio_file, beam_size=5)
    return segments

def append_to_transcript(transcript_file, text):
    with open(transcript_file, "a") as f:
        f.write(text)

def seg():
    while True:
        audio_files = glob.glob(audio_file_pattern)
        
        if len(audio_files) < 2:
            time.sleep(5)  
            continue
        
        audio_files.sort() 
        
        for audio_file in audio_files:
            segments = transcribe_audio(audio_file)
            
            if segments:
                with open(output_transcript_file, "a") as f:
                    for segment in segments:
                        f.write(f"\n{segment.text}")
                    
                    
                os.remove(audio_file)
        
        time.sleep(5) 

