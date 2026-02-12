# MP3 AudioTransposer
**This Project Changes the Semitones of a song between loop cycles ranging from -12 to +12:**




**HERE -12 semitone makes the song sound DEEPER,DARKER and invokes a feeling of listening to the voices of demonic spirits whereas +12 semitone makes the song sound BRIGHTER,JOYFUL and gives the listener the feel of ascending to the heavens by hearing angelic voices....**

 * The lower you go in semitones, the voice becomes deeper and darker.
 * The higher you go in semitones , the voice becomes higher-pitched and brighter.

This project is A keyboard-controlled MP3 pitch-shifting player that renders and plays all semitone transpositions from -12 to +12, with instant stepping, loop modes, and song switching — built with Python + SoX + ffplay+DSP transforms and subprocess audio streaming.

Designed as a fast interactive transpose explorer for music practice, pitch testing, and audio experimentation.

**...................................................................................................................................................................................................................**






**🧪 WHAT THIS TOOL IS  PERFECT FOR:**

🎤 Vocal range practice:
**When you upload instrumentals of a song and want to see which semitone best suits your voice for singing purposes.**

🎹 Ear training:
**Usually to make your hearing sharper by focusing on filters,background noises and sound clarity.**

🎧 Key detection experiments:
**For Musicians to compose or generate new ideas for instrumentals by observing what scale is used which notes are stable.**

🎼 Transpose study:
**Many students listen to songs and study..Supposedly some prefer playing the same songs while studying.. but listening to the same voice and the same pitch again and again makes one feel bored and they end up losing interest in studies...In order to overcome this issue ,this tool plays different versions of the same song and makes us understand the hidden feeling thus keeping curiosity intact.**

🔊 Sound design testing:
**Can be used for Audio QA testing and testing sound semitones in FX Designing and games**

**Ex: A Princess's voice can be either deeper,Anime style +3 to +5 semitones and so on....**

💡 DSP
**Analysts and Researchers:**
* *resampling*
* *spectral processing*
* *phase adjustment*
* *frequency scaling*

**...................................................................................................................................................................................................................**

**🎧 CORE KEY FEATURES:**

1.🎵 Multi-Semitone Pitch Transposition:

* *Generates pitch-shifted audio from -12 to +12 semitones*
* *Uses SoX pitch transform for proper audio shifting*
* *Pre-renders all versions for instant switching*

**...................................................................................................................................................................................................................**

2.⌨️ Real-Time Keyboard Control System:

* *Live hotkey controls during playback*
* *No UI needed — pure keyboard command mode*
* *Instant response stepping between pitches*

**...................................................................................................................................................................................................................**

3.🔁 Dual Loop Modes:

* *Bounce mode: auto steps between -12 ↔ +12*
* *Lock mode: repeats same semitone forever*
* *Toggleable live during playback*

**...................................................................................................................................................................................................................**

4.📂 Automatic MP3 Detection:

* *Scans script folder for MP3 files*
* *Dynamic song list generation*
* *User selection by index*
* *Wraparound navigation between songs*

**...................................................................................................................................................................................................................**

5.🧱 Modular Function Structure:

* *pitch shift function*
* *render pipeline*
* *stepping logic*
* *song navigation*
* *control loop*

**...................................................................................................................................................................................................................**


**⚙️ HOW IT ACTUALLY WORKS:**

* *The program scans the script folder for MP3 files and lets the user select one.*
* *The selected track is loaded and converted to WAV format.*
* *Using SoX pitch transformation, the audio is rendered into 25 shifted versions (−12 to +12 semitones).*
* *All shifted files are stored temporarily for fast switching.*
* *Audio playback is handled by ffplay in headless mode.*
* *Keyboard hotkeys control pitch stepping, song switching, and loop behavior in real time.*
* *Boundary logic prevents repeated edge semitones and keeps stepping smooth.*
* *Temp files are cleaned automatically before each new render cycle.*

**...................................................................................................................................................................................................................**


**🧰 PREREQUISITES:**

*Make sure these are installed on your system before running the script:*
* *Python 3.9 or higher
* *FFmpeg (must include ffplay)
* *SoX (Sound eXchange)
* *Windows OS (recommended — hotkeys tested here)
* *Python packages required:
* *pydub
* *sox
* *keyboard

**...................................................................................................................................................................................................................**

**📦 INSTALLATION:**

Clone the repository:

```bash
git clone https://github.com/InventorBlackFox/AudioTransposer.git
cd AudioTransposer
```

**...................................................................................................................................................................................................................**

**Install required Python packages:**
```bash
pip install pydub sox keyboard
```

**...................................................................................................................................................................................................................**

**🎵 EXTERNAL TOOLS SETUP:**

**...................................................................................................................................................................................................................**

**FFmpeg + ffplay**

* **Install FFmpeg and make sure ffmpeg and ffplay are available in your system PATH.**
* **Test in terminal:**
```bash
 ffmpeg -version
```
```bash
 ffplay -version
```
* **If both print version info — you’re good.**

**...................................................................................................................................................................................................................**

**SoX**

* **Install SoX and ensure it is added to PATH.**

* **Test:**
```bash
 sox --version
```

**...................................................................................................................................................................................................................**

**📁 HOW TO RUN:**

* **1️⃣ Put the Python script inside a folder**
* **2️⃣ Place your MP3 files in the same folder**
* **3️⃣ Click the address bar(Navigation Bar)**
* **4️⃣ Type cmd above in the adress bar and press enter**
* **5️⃣ Now type inside cmd this: *python Audio_transposer.py***


Make sure this folder path exists or can be created.

**...................................................................................................................................................................................................................**


**🔧 TECHNOLOGIES AND SOFTWARES USED:**

* **PYTHON**
* **STANDARD LIBRARIES like os,subprocess,time**
* **PYDUB**
* **sox(PYTHON WRAPPER)**
* **SoX ENGINE(EXTERNAL BINARY)**
* **FFmpeg / FFplay**
* **KEYBOARD**
* **MP3 AND WAV FILE FORMATS INVOLVED**

**...................................................................................................................................................................................................................**


**⚠️ NOTES:**

* **Terminal window must stay focused for hotkeys**
* **First render takes time (creates all 25 pitch versions)**
* **Designed for Windows environment (path + keyboard lib)**
* **On Linux/macOS, global hotkeys may require running with elevated permissions or may behave differently depending on the window system**

**...................................................................................................................................................................................................................**
**...................................................................................................................................................................................................................**
