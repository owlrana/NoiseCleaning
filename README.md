# NoiseCleaning
# Automatically detects and removes noise from Audio Files
_**Rahul Rana**, Assisted by: **Jeannine Hamade**_
____________________________

**Abstract:**

_The fundamental aim of this project is to automate the process of Audio Cleaning before Audio Mixing for Voice-Overs or Audio Recordings in videos. This is achieved by the following features: '**Selecting a noise base** (to set-up and store the information about noise floor', '**De-Noising the file using previously selected base** (to mute sections containing ONLY the noise floor and imitating de-Noise plugin with EQ', '**controlling dynamics:** **Compression** (modifiable Threshold [-60dB to 0dB], Ratio [1:1 to 1:30], Make-Up Gain [-20 to 50 dB], Attack [0 to 200 ms], Release [ 5 to 5k ms]), **Limiter**, **Equalization** (Channel, Linear, Match, Single Band), and finally **Normalisation** (Increasing the final Signal to anywhere between -1 dB to -0.1dB to prevent distortion)_

____________________________

**Special Thanks to:**

**_FFmpeg_** - Wonderful collection of libraries and tools to process multimedia content such as audio, video, subtitles and related metadata.
Link: https://github.com/FFmpeg/FFmpeg

**_Sox_** - They call themselves the "Swiss Army Knife of Sound Processing" and man oh man they really are!
Link: http://sox.sourceforge.net

**_Audacity_** - This software (Audio Editor) is a go-to place for any User who wants to create content (Available on Linux, MacOS & Windows). It is plain. It is simple. The best thing: It is Open-Sourced! The repositories avaiable are giving a new life to this project and once I create a fully-functionaing scripts it will help me complete the sound-cleanup using their **TOP CLASS** algorithms that work through Machine Learning and a lot of other concepts currently beyond my grasp (lol).
https://github.com/audacity/audacity

____________________________

**References:**

(1) Technology of Music Production
    Berkley School of Music
    https://www.coursera.org/learn/technology-of-music-production/
    
(2) Y. Dong, R.H. Chan, S. Xu
    A detection statistic for random-valued impulse noise
    IEEE Trans. Image Process, 16 (2007), pp. 1112-1120
    Google Scholar
    https://ieeexplore.ieee.org/abstract/document/4130419/
    
(3) J. Nuzman, Audio Restoration: An Investigation of Digital Methods for Click Removal and Hiss Reduction, Jan, 2004.
    Google Scholar
    https://pdfs.semanticscholar.org/eccb/50f9a37b1bf77afd1e5457ac276cdb1a5c09.pdf
