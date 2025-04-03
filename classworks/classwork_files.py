"""
(c) 2025 - Justus Decker - coding solution

(c) Masterschool

🎭 Writing Exercise: Romeo and Juliet 📜

## **Hey there, Scripting Shakespeare Enthusiast!**

Let’s practice working with files in these exercises using Shakespeare's masterpiece, "Romeo and Juliet"! 🌹 [**Download the file here](https://www.mediafire.com/file/qaur1h2p94e6mzo/romeo_and_juliet.txt/file).** Let's dive right into the action! 

## **Exercises 📝**

### **Exercise 1: Swap Names! 💑**

🔁 **Task:** Create your twist by swapping the names of Romeo and Juliet. 
Let's make "Jack and Rose" sail through love instead! 
Create a new file named "jack_and_rose.txt", where every "Romeo" is replaced with "Jack", and every "Juliet" is replaced with "Rose".

### **Exercise 2: Word Frequency Analysis 📊**

📝 **Task:** Conduct a word frequency analysis on the text from "romeo_and_juliet.txt". Create a new file named "word_frequency.txt", where each unique word from the play is listed along with its frequency.🖋️

### **Bonus Exercise: Amplify Your Musical Journey! 🎵**

🎶 **Task:** You have a beloved song in a file named [**"celine.mp3"**](https://www.mediafire.com/file/j5raq6qi7dz0aqt/celine.mp3/file), 
but the last 40 seconds of the song is mostly silent! 
This makes for an annoying listening experience when you put your song in a playlist. 
Write a Python script to cut out the last 10 percent of the track. 
Save the cut version to a new file named "celine_shorter.mp3". 
Let the music play on! 🎧🎵
"""

#A simple read & write example in python. No check for OSError etc.
from os import path
def read(file:str) -> str | bool:
    if path.isfile(file):
        with open(file,"r") as f_in:
            return f_in.read()
    else:
        print(f"{file} cannot be found!")
        return False
def write(file:str,data:str) -> None:
    with open(file,"w") as f_out:
        return f_out.write(data)
def bubble_sort(array1,array2):
    n = len(array1)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array1[j] > array1[j + 1]:
                array1[j], array1[j + 1] = array1[j + 1], array1[j]
                array2[j], array2[j + 1] = array2[j + 1], array2[j]
    array1.reverse(),array2.reverse()
    return array1[:10],array2[:10]

print("**Exercise 1: Swap Names! 💑**")
STORY = read("romeo_and_juliet.txt")
for before,after in [("Romeo","Kevin"),("Juliet","Babara")]:
    for b,a in [(before.upper(),after.upper()),(before.lower(),after.lower()),(before.capitalize(),after.capitalize())]:
        STORY = STORY.replace(b,a)

write("kevin_love_story.txt",STORY)

print("**Exercise 2: Word Frequency Analysis 📊**")
hashmap = {word: STORY.count(word) for word in STORY.split(" ") if word}

scores,words = bubble_sort([hashmap[key] for key in hashmap],[key for key in hashmap])
for score,word in zip(scores,words):
    print(f"{word:<15}: {score}")

print("**Bonus Exercise: Amplify Your Musical Journey! 🎵**")
from subprocess import run,CREATE_NO_WINDOW
from os import path
from moviepy.audio.io.AudioFileClip import AudioFileClip
def get_audio_length(filename):
    if path.isfile(filename):
        return AudioFileClip(filename).duration
    return -1
def cut_audio(fromname:str,toname:str):
            run(
                [
                    'ffmpeg',
                    "-to",
                    f"{get_audio_length(fromname)*.9}",
                    '-n',
                    '-i',
                    fromname,
                    toname
                    ],
                    CREATE_NO_WINDOW,
                    shell= True
                )
cut_audio("celine.mp3","celine_shorter.mp3")
