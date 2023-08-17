import subprocess
import time
import glob
import os
import threading
import transcription, menu

def cleanup_previous_files():
    for f in glob.glob("audio_output_file_*.flac"):
        os.remove(f)

def capture():
    twitch_url = stream
    output_base = "audio_output_file"
    output_format = "flac"
    slice_index = 1

    while True:
        audio_output_file = f"{output_base}_{slice_index}.{output_format}"
        streamlink_cmd = f"streamlink -o {audio_output_file} --twitch-disable-ads {twitch_url} audio_only"
        subprocess.Popen(streamlink_cmd, shell=True)

        time.sleep(sleep_time)

        streamlink_pid = subprocess.check_output(["pgrep", "streamlink"]).decode("utf-8").strip()
        if streamlink_pid:
            subprocess.Popen(["kill", streamlink_pid])
        else:
            subprocess.Popen(streamlink_cmd, shell=True)
        slice_index += 1  

if __name__ == "__main__":

    menu.cli()

    while True:
        stream = input("Enter the URL of the stream to be transcribed (e.g. https://www.twitch.tv/mystream): ")
        if stream.strip() != "":
            break
        print("URL cannot be empty. Please enter a valid URL.")

    while True:
        sleep_time = input("Enter time intervals (default is 30 seconds): ")
        if sleep_time.strip() == "":
            sleep_time = 48
            break
        try:
            sleep_time = int(sleep_time)
            if sleep_time > 0:
                break
            else:
                print("Time interval should be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid time interval.")

    cleanup_previous_files()
    
    capture_thread = threading.Thread(target=capture)
    transcription_thread = threading.Thread(target=transcription.seg)
    
    capture_thread.start()
    transcription_thread.start()

    capture_thread.join()
    transcription_thread.join()

