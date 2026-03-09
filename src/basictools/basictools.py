import sounddevice as sd
import soundfile as sf

def title2(text):
    """Returns a superior title case from default title()"""
    return ' '.join(word.capitalize() for word in text.split(' '))

def play_sound(path, stop_terminal=False,debug_statements=False):
    data, fs = sf.read(path, dtype="float32")
    if debug_statements == True:
        print(f"playing {path}")
    sd.play(data, fs)
    if stop_terminal == True:
        if input("Press ENTER to stop the sound: \n") == (""):
            sd.stop()
    sd.wait()
    if debug_statements == True:
        print("playing finished")
