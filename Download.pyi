from .SaveBlock import *
from .LowLevel import LowLevel


class Download:
    """
        The Download class provides functionality for downloading music from the internet.

        Methods:
        --------
        youtube(filename: str)
        """
    @staticmethod
    def youtube(filename: str):
        """
        Download music from YouTube using information from the specified msbf file.

        Parameters:
        -----------
        filename : str
            The name of the msbf file.

        Notes:
        ------
        1) The file should be in the msbf format.
        2) Music files are going to be downloaded to ./artist/album

        Example:
        --------
        >>> libmsb.Download.youtube("example.msbf")
        """
        file = Msbf.IO.load(filename)
        LowLevel.Download.create_address(file["Base"]["Artist"], file["Base"]["Album"])

        for item in file["Music"]:
            write_data = LowLevel.Download.download_youtube(item["ID"])
            open(item["Title"] + ".mp3", "wb").write(write_data)

        LowLevel.Download.clean_address()