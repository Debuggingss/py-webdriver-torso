# py-webdriver-torso
Render videos like Webdriver Torso

[![python](https://img.shields.io/badge/python-v3.8.3-green?style=for-the-badge)](https://www.python.org/downloads/release/python-383/)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


Webdriver Torso: https://www.youtube.com/channel/UCsLiV4WJfkTEHH0b9PmRklw/videos

Requirements:
- Python 3.8+
- moviepy
- Pillow
- pydub
- Wave
- ffmpeg

ffmpeg: https://ffmpeg.org/

Optimal (default) configuration:
```json
{
  "WIDTH": 640,
  "HEIGHT": 360,
  "MAX_WIDTH": 640,
  "MAX_HEIGHT": 360,
  "MIN_WIDTH": 0,
  "MIN_HEIGHT": 0,
  "SLIDES": 10,
  "VIDEOS": 10,
  "SOUND_QUALITY": 14000.0
}
```
WARNING: While testing the lowest sound quality possible was 14,000 for me. The higher the sound quality is the longer it takes to render the video(s). It does not change 
