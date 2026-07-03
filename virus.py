import time
import urllib.request
import winsound
 
# Any direct link to a .wav file works. This one is a short, freely
# licensed "boop" sound effect. Swap the URL for any .wav you like.
SOUND_URL = "https://www.myinstants.com/media/sounds/fart-with-reverb.mp3"
 
def download_sound(url: str) -> str:
    tmp_dir = tempfile.gettempdir()
    local_path = os.path.join(tmp_dir, "loop_sound_effect.wav")
 
    # Only download if we don't already have it cached locally.
    if not os.path.exists(local_path):
        urllib.request.urlretrieve(url, local_path)
 
    return local_path
 
def main():
    try:
        wav_path = download_sound(SOUND_URL)
    except Exception as e:
        # If offline / download fails, bail out cleanly.
        sys.exit(f"Failed to download sound: {e}")
 
    # SND_LOOP + SND_ASYNC makes Windows loop the sound in the background
    # forever, without blocking this script.
    winsound.PlaySound(wav_path, winsound.SND_LOOP | winsound.SND_ASYNC)
 
    try:
        # Keep the process alive so the loop keeps playing.
        # Kill it via Task Manager (look for "pythonw.exe" / "python.exe")
        # or Ctrl+C if you launched it with "python" in a visible console.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        winsound.PlaySound(None, winsound.SND_PURGE)  # stop playback
 
if __name__ == "__main__":
    main()
