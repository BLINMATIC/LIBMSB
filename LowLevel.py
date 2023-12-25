import os
import subprocess
from .Config import Config


class LowLevel:
    class Download:
        @staticmethod
        def create_address(artist, album):
            try:
                os.mkdir(artist)
            except:
                pass

            try:
                os.mkdir(os.path.join(artist, album))
            except:
                pass

            os.chdir(os.path.join(artist, album))

        @staticmethod
        def download_youtube(vid):
            subprocess.run([Config.YTDLP_PATH, "--ffmpeg-location", Config.FFMPEG_PATH, "-x", "--audio-format", "mp3", "-o", "tmp.mp3", f"https://www.youtube.com/watch?v={vid}"], capture_output=False, text=False)
            output = open("tmp.mp3", "rb").read()
            os.remove("tmp.mp3")

            return output

        @staticmethod
        def clean_address():
            os.chdir("../../")