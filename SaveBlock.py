from .Config import Config
import json


class Msbf:
    class Element:
        @staticmethod
        def base(artist, album, release_date):
            return {"Artist": artist, "Album": album, "Year": release_date}

        @staticmethod
        def music(artist, title, queue_number, download_id):
            return {"Artist": artist, "Title": title, "Number": queue_number, "ID": download_id}

        @staticmethod
        def full(base, music_list):
            return {"Base": base, "Music": music_list, "Version": Config.VERSION_ID}

    class IO:
        @staticmethod
        def create(full, filename):
            open(filename + ".msbf", "w").write(json.dumps(full))

        @staticmethod
        def load(filename):

            return json.loads(open(filename, "r").read())

