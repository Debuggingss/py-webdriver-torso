import random
from PIL import Image, ImageDraw, ImageFont
import math
import random
import wave
import struct
from pydub import AudioSegment
import os
import moviepy.video.io.ImageSequenceClip
import glob
import json

class JSON:
    def read(file):
        with open(f"{file}.json", "r", encoding="utf8") as file:
            data = json.load(file)
        return data

    def dump(file, data):
        with open(f"{file}.json", "w", encoding="utf8") as file:
            json.dump(data, file, indent=4)

config_data = JSON.read("config")

# SETTINGS #
w = config_data["WIDTH"]
h = config_data["HEIGHT"]
maxW = config_data["MAX_WIDTH"]
maxH = config_data["MAX_HEIGHT"]
minW = config_data["MIN_WIDTH"]
minH = config_data["MIN_HEIGHT"]
LENGTH = config_data["SLIDES"]
AMOUNT = config_data["VIDEOS"]
sample_rate = config_data["SOUND_QUALITY"]
# SETTINGS #

fnt = ImageFont.truetype("./FONT/sys.ttf", 10)

files = glob.glob('./IMG/*')
for f in files:
    os.remove(f)

print("REMOVED OLD FILES")


def generate_string(length):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = ""
    for i in range(length):
        result += random.choice(charset)
    return result


def append_sinewave(
        freq=random.randint(70, 200) * 10,
        duration_milliseconds=1000,
        volume=1.0):

    global audio

    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * ( x / sample_rate )))
    return


def save_wav(file_name):
    wav_file = wave.open(file_name, "w")

    nchannels = 1

    sampwidth = 2

    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    for sample in audio:
        wav_file.writeframes(struct.pack('h', int(sample * 32767.0)))

    wav_file.close()

    return


for xyz in range(AMOUNT):
    for i in range(LENGTH):
        shapeR = [(random.randint(0, w), random.randint(0, h)), (random.randint(minW, maxW), random.randint(minH, maxH))]
        shapeB = [(random.randint(0, w), random.randint(0, h)), (random.randint(minW, maxW), random.randint(minH, maxH))]

        img = Image.new("RGB", (w, h))

        img1 = ImageDraw.Draw(img)

        img1.rectangle([(0, 0), (w, h)], fill="white", outline="white")

        img1.rectangle(shapeR, fill="red", outline="red")
        img1.rectangle(shapeB, fill="blue", outline="blue")
        name = generate_string(10)
        img1.text((1, h-20), "aqua.flv - Slide " + str(i).zfill(4), font=fnt, fill="black")
        img.save("./IMG/" + str(i).zfill(4) + ".png")

    print("IMAGE GENERATION DONE")

    audio = []

    for i in range(LENGTH):
        append_sinewave(random.randint(700, 2000), volume=0.25)

    save_wav("./SOUND/output.wav")

    print("WAV GENERATED")

    wav_audio = AudioSegment.from_file("./SOUND/output.wav", format="wav")

    wav_audio.export("./SOUND/output.mp3", format="mp3")

    print("MP3 GENERATED")

    image_folder = './IMG'
    fps = 1

    image_files = [image_folder + '/' + img for img in os.listdir(image_folder) if img.endswith(".png")]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    name = generate_string(6)
    clip.write_videofile('./OUTPUT/tmp' + name + '.mp4', audio="./SOUND/output.mp3")

    print("FINISHED - FILE NAME: tmp" + name + ".mp4")
