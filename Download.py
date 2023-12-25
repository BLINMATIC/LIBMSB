from .SaveBlock import *
from .LowLevel import LowLevel


class Download:
    @staticmethod
    def youtube(filename):
        file = Msbf.IO.load(filename)
        LowLevel.Download.create_address(file["Base"]["Artist"], file["Base"]["Album"])

        for item in file["Music"]:
            write_data = LowLevel.Download.download_youtube(item["ID"])
            open(item["Title"] + ".mp3", "wb").write(write_data)

        LowLevel.Download.clean_address()