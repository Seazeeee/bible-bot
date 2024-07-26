import json
import requests


class Versus():

    def __init__(
        self, book: str, chapter: int, verse=None, translation=None
    ):

        english_translations_dict = {
            "YLT",
            "KJV",
            "NKJV",
            "WEB",
            "RSV",
            "CJB",
            "TS2009",
            "LXXE",
            "TLV",
            "LSB",
            "NASB",
            "ESV",
            "GNV",
            "DRB",
            "NIV2011",
            "NIV",
            "NLT",
            "NRSVCE",
            "NET",
            "NJB1985",
            "SPE",
            "LBP",
            "AMP",
            "MSG",
            "LSV",
            "BSB",
        }

        self.book = book
        self.chapter = chapter
        self.verse = verse

        if translation == None or translation not in english_translations_dict:
            self.translation = "ESV"
        else:
            self.translation = translation

    def pullVerse(self):
        url = "http://bolls.life/get-verses/"  # Replace with your actual endpoint URL

        payload = [
            {
                "translation": "ESV",  # self.translation,
                "book": "Matthew",  # self.book,
                "chapter": 1,  # self.chapter,
                "verses": [1, 2, 3]  # [self.verse],
            },
        ]

        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(
                url, headers=headers, data=json.dumps(payload), timeout=10
                )
            response.raise_for_status()  # Raise error for bad status codes

            data = response.json()
            print(data)  # Output the response JSON data

        except requests.exceptions.RequestException as e:
            print("Error:", e)

