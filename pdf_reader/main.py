# Python imports
from ebook_to_text import epub2text
import vlc
import time
import keyboard

# Sets file path
FILE_PATH = "thenamesake.epub"
RATE = 300
SKIP_AMOUNT = 5000 # in milliseconds


# Processes epub
chapters = epub2text(FILE_PATH)
# Formats chapter to be a big string
display_chapters = "\n".join(["{}: {}...".format(i, chapters[i][:50].replace("\n", " ").strip())
                              for i in range(0, len(chapters))]) + "\nChoose which chapter you would like to start at by typing in the number corresponding to that chapter: "
# Lets user choose chapter through input
start_chapter = int(input(display_chapters))
rate = int(input("How fast (in words per minute) do you want the narration to be (recommended: 200, max: 300)? "))


from text_to_wav import TextToWAV
TextToWAV(text=chapters[start_chapter], output_path="audio.wav", rate=rate)


# Sets up VLC player
p = vlc.MediaPlayer("audio.wav")
p.play()


# Pauses (down arrow)
def pause_play():
    is_playing = p.is_playing()
    if is_playing == False:
        p.play()
    else: # (if playing == False)
        p.pause()


# Forward skip (right arrow)
def forward():
    audio_time = p.get_time()
    time_to_skip_to = min(audio_time + SKIP_AMOUNT, p.get_length())
    p.set_time(time_to_skip_to)


# Backward skip (left arrow)
def backward():
    audio_time = p.get_time()
    time_to_skip_to = max(audio_time - SKIP_AMOUNT, 0)
    p.set_time(time_to_skip_to)

def get_time():
    audio_time = p.get_time()
    print(audio_time)

# Adds hotkeys
keyboard.add_hotkey('right', forward)
keyboard.add_hotkey('left', backward)
keyboard.add_hotkey('down', pause_play)
keyboard.add_hotkey('up', get_time)

keyboard.wait()