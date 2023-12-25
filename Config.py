import os


class Config:
    VERSION = "100-100 359/2023"
    VERSION_ID = 1

    START_PATH = os.getcwd()
    YTDLP_PATH = os.path.join(START_PATH, "libext/yt-dlp.exe")
    FFMPEG_PATH = os.path.join(START_PATH, "libext/ffmpeg/bin/ffmpeg.exe")
