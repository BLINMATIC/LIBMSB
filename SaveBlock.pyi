from .Config import Config
import json


class Msbf:
    """
        The Msbf class provides functionality for working with msbf (Music Storage Block File) files.

        Classes:
        --------
        Element
            Contains static methods for creating different elements of a msbf file, such as base and music entries.

        IO
            Contains static methods for handling input and output operations on msbf files.
        """
    class Element:
        """
        The Element class contains static methods for creating different elements of an Msbf file.

        Methods:
        --------
        base(artist: str, album: str, release_date: int)
            Create a base element for a msbf file.

        music(artist: str, title: str, queue_number: int, download_id: str)
            Create a music element for a msbf file.

        full(base: dict, music_list: list)
            Create a full msbf element containing both base and music entries.
        """

        @staticmethod
        def base(artist: str, album: str, release_date: int) -> dict:
            """
            Create a base element for a msbf file.

            Parameters:
            -----------
            artist : str
                The name of the artist.
            album : str
                The title of the album.
            release_date : int
                The release date of the album.

            Returns:
            --------
            dict
                A dictionary representing the base element.

            Example:
            --------
            >>> base_info = Msbf.Element.base("İbrahim Tatlıses", "Türkü Dinle Türkü Söyle Türkü Oyna", 1998)
            """

        @staticmethod
        def music(artist: str, title: str, queue_number: int, download_id: str) -> dict:
            """
            Create a music element for a msbf file.

            Parameters:
            -----------
            artist : str
                The name of the artist.
            title : str
                The title of the music.
            queue_number : int
                The queue number of the music in the album.
            download_id : str
                The download id for a website.

            Returns:
            --------
            dict
                A dictionary representing the music element.

            Example:
            --------
            >>> music_info = Msbf.Element.music("İbrahim Tatlıses", "Adana Köprü Başı", 2, "q2-_smydYdM")
            """

        @staticmethod
        def full(base: dict, music_list: list):
            """
            Create a full msbf element containing both base and music entries.

            Parameters:
            -----------
            base : dict
                The base element of the msbf file.
            music_list : list
                A list of music elements.

            Returns:
            --------
            dict
                A dictionary representing the full msbf element.

            Example:
            --------
            >>> base_info = Msbf.Element.base("İbrahim Tatlıses", "Türkü Dinle Türkü Söyle Türkü Oyna", 1998)
            >>> music_info1 = Msbf.Element.music("İbrahim Tatlıses", "Adana Köprü Başı", 2, "q2-_smydYdM")
            >>> music_info2 = Msbf.Element.music("İbrahim Tatlıses", "Emmine", 3, "KLO0P_7QyKY")
            >>> full_info = Msbf.Element.full(base_info, [music_info1, music_info2])
            """
    class IO:
        """
        The IO class contains static methods for handling input and output operations on msbf files.

        Methods:
        --------
        create(full: dict, filename: str)
            Create a msbf file from full dict.

        load(filename: str)
            Load a msbf file from disk and return its contents as a dict.
        """

        @staticmethod
        def create(full: dict, filename: str) -> None:
            """
            Create a msbf file from full dict.

            Parameters:
            -----------
            full : dict
                The full Msbf element to be saved.
            filename : str
                The name of the file (without extension) to be created.

            Example:
            --------
            >>> base_info = Msbf.Element.base("İbrahim Tatlıses", "Türkü Dinle Türkü Söyle Türkü Oyna", 1998)
            >>> music_info1 = Msbf.Element.music("İbrahim Tatlıses", "Adana Köprü Başı", 2, "q2-_smydYdM")
            >>> music_info2 = Msbf.Element.music("İbrahim Tatlıses", "Emmine", 3, "KLO0P_7QyKY")
            >>> full_info = Msbf.Element.full(base_info, [music_info1, music_info2])
            >>> Msbf.IO.create(full_info, "example1")
            """
        @staticmethod
        def load(filename: str) -> dict:
            """
            Load a msbf file from disk and return its contents as a dict.

            Parameters:
            -----------
            filename : str
                The name of the Msbf file to be loaded.

            Returns:
            --------
            dict
                The contents of the Msbf file.

            Example:
            --------
            >>> loaded_data = Msbf.IO.load("input_file.msbf")
            """