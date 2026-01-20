import os, subprocess, time, sox
from pydub import AudioSegment
import keyboard

TEMP_DIR = r"D:\ffmpeg_temp"
os.makedirs(TEMP_DIR, exist_ok=True)

folder = os.path.dirname(os.path.abspath(__file__))
mp3_files = [f for f in os.listdir(folder) if f.lower().endswith(".mp3")]

if not mp3_files:
    raise FileNotFoundError("💀 No MP3 files found in this folder!")

print("\n🎧 Available MP3 files:")
for i, f in enumerate(mp3_files, start=1):
    print(f"{i}. {f}")

song_index = int(input("\n👉 Enter the number of the MP3 you want to transpose: ")) - 1
song_index %= len(mp3_files)


def shift_pitch(sound, semitones, outfile):
    temp_in = os.path.join(TEMP_DIR, "input.wav")
    sound.export(temp_in, format="wav")
    tfm = sox.Transformer()
    tfm.set_globals(verbosity=0)
    tfm.pitch(semitones)
    tfm.build(temp_in, outfile)


def render_song(audio_file):
    print(f"\n🔥 Loading: {audio_file}")
    audio = AudioSegment.from_file(audio_file)

    # 🧹 Clean temp folder
    for f in os.listdir(TEMP_DIR):
        if f.startswith("shift_") and f.endswith(".wav"):
            try:
                os.remove(os.path.join(TEMP_DIR, f))
            except OSError:
                pass

    files = []
    for s in range(-12, 13):
        out = os.path.join(TEMP_DIR, f"shift_{s:+}.wav")
        print(f"Rendering {s:+} semitones…")
        shift_pitch(audio, s, out)
        files.append(out)

    return files


def semitone_from_index(index):
    return index - 12  # index 12 = 0 semitones


# ✅ FIXED: no endpoint repeat
def step_index(index, direction):
    """
    Moves by direction.
    If endpoint reached, flips direction and moves away immediately.
    Prevents repeating -12 or +12.
    """
    new_index = index + direction

    if new_index < 0:  # hit -12 boundary
        direction = +1
        new_index = index + direction

    elif new_index > 24:  # hit +12 boundary
        direction = -1
        new_index = index + direction

    return new_index, direction


def next_song():
    global song_index, files, index, direction
    song_index = (song_index + 1) % len(mp3_files)
    files = render_song(mp3_files[song_index])
    index = 12
    direction = -1


def prev_song():
    global song_index, files, index, direction
    song_index = (song_index - 1) % len(mp3_files)
    files = render_song(mp3_files[song_index])
    index = 12
    direction = -1


files = render_song(mp3_files[song_index])

index = 12
direction = -1

print("\n🎮 CONTROLS (NO FREEZE ✅ + NO EDGE REPEAT ✅):")
print("   CTRL + →    = +1 semitone")
print("   CTRL + ←    = -1 semitone")
print("   CTRL + ↑    = Next song")
print("   CTRL + ↓    = Previous song")
print("   CTRL + ESC  = Quit")
print("\n💡 Keep terminal focused to control playback.\n")

player = None

cooldown = 0.18
last_press_time = 0

while True:
    path = files[index]
    semitone = semitone_from_index(index)
    print(f"🎵 Playing {semitone:+} semitones | Song {song_index+1}/{len(mp3_files)}")

    player = subprocess.Popen(
        ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", path],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    while player.poll() is None:
        now = time.time()

        if now - last_press_time >= cooldown:

            if keyboard.is_pressed("ctrl+esc"):
                player.kill()
                print("👋 Exiting. CTRL+ESC executed. Audio shutdown complete 🎧🫡")
                raise SystemExit

            if keyboard.is_pressed("ctrl+right"):
                player.kill()
                direction = +1
                index, direction = step_index(index, direction)
                last_press_time = now
                break

            if keyboard.is_pressed("ctrl+left"):
                player.kill()
                direction = -1
                index, direction = step_index(index, direction)
                last_press_time = now
                break

            if keyboard.is_pressed("ctrl+up"):
                player.kill()
                next_song()
                last_press_time = now
                break

            if keyboard.is_pressed("ctrl+down"):
                player.kill()
                prev_song()
                last_press_time = now
                break

        time.sleep(0.01)

    else:
        # ✅ auto continue same direction, no endpoint repeat
        index, direction = step_index(index, direction)
