TwitchToText - transcription
====================================

TwitchToText is a tool that allows you to transcribe a Twitch live stream. It uses the `faster_whisper` transcription template for audio-to-text conversion. Make sure you have installed the modules listed in the `requirements.txt` file and install streamlink before running the script.

Installation instructions :
-----------------------------
1. Make sure you have Python installed on your system.
2. Install the required modules by running the following command:
```
pip install -r requirements.txt
```
or manually install each of these modules:
```
pip install colorama
pip install faster_whisper
```
And install streamlink according to your system (the doc is here: https://streamlink.github.io/install.html), for example if you're based on debian:
```
sudo apt install streamlink
```
3. Make sure you have the `faster_whisper` transcription template correctly installed and configured.
4. Run the `main.py` file to launch the audio stream capture and transcription script.

Usage:
-------------
1. Run the `main.py` script.
2. Follow the instructions to provide the URL of the streaming audio stream you wish to transcribe.
3. Choose the time interval between audio segment captures (can be ignored),
the longer the time interval, the better the quality and fidelity of the transcription, but the greater the performance required.
5. The transcription results will be saved in the `transcript.txt` file.
6. The program waits for at least two time intervals to be captured before starting transcription, so don't worry if the result doesn't appear immediately in the file - it may take several minutes.
7. Stop the script by pressing Ctrl+C.

Author:
--------
opnsh

For more information and updates, see the project's GitHub repository: https://github.com/opnsh/TwitchToText-transcription
