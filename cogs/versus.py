import json
import difflib
import requests
import bleach
import re


class versus():

    def __init__(
        self, book: str, chapter: int, verse_start: int, verse_end: int, translation=None
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
        self.verse_start = verse_start
        self.verse_end = verse_end

        if translation == None or translation not in english_translations_dict:
            self.translation = "ESV"
        else:
            self.translation = translation

    def pullVerses(self):
        library = {
            1: "Genesis",
            2: "Exodus",
            3: "Leviticus",
            4: "Numbers",
            5: "Deuteronomy",
            6: "Joshua",
            7: "Judges",
            8: "Ruth",
            9: "1 Samuel",
            10: "2 Samuel",
            11: "1 Kings",
            12: "2 Kings",
            13: "1 Chronicles",
            14: "2 Chronicles",
            15: "Ezra",
            16: "Nehemiah",
            17: "Esther",
            18: "Job",
            19: "Psalm",
            20: "Proverbs",
            21: "Ecclesiastes",
            22: "Song of Solomon",
            23: "Isaiah",
            24: "Jeremiah",
            25: "Lamentations",
            26: "Ezekiel",
            27: "Daniel",
            28: "Hosea",
            29: "Joel",
            30: "Amos",
            31: "Obadiah",
            32: "Jonah",
            33: "Micah",
            34: "Nahum",
            35: "Habakkuk",
            36: "Zephaniah",
            37: "Haggai",
            38: "Zechariah",
            39: "Malachi",
            40: "Matthew",
            41: "Mark",
            42: "Luke",
            43: "John",
            44: "Acts",
            45: "Romans",
            46: "1 Corinthians",
            47: "2 Corinthians",
            48: "Galatians",
            49: "Ephesians",
            50: "Philippians",
            51: "Colossians",
            52: "1 Thessalonians",
            53: "2 Thessalonians",
            54: "1 Timothy",
            55: "2 Timothy",
            56: "Titus",
            57: "Philemon",
            58: "Hebrews",
            59: "James",
            60: "1 Peter",
            61: "2 Peter",
            62: "1 John",
            63: "2 John",
            64: "3 John",
            65: "Jude",
            66: "Revelation",
        }

        for key, value in library.items():
            if value == self.book:
                exact_match = key
                break
            else:
                close_matches = difflib.get_close_matches(
                    self.book, library.values(), n=1
                )
                if close_matches:
                    close_match_title = close_matches[0]
                    for key, value in library.items():
                        if value == close_match_title:
                            exact_match = value
                            break

        bookId = exact_match
        # https://bolls.life/get-verse/<slug:translation>/<int:book>/<int:chapter>/<int:verse>/

        verse_block = ""
        count = self.verse_start

        while count <=self.verse_end:
            
            verse_url = (
                "https://bolls.life/get-verse/"
                + str(self.translation).upper()
                + "/"
                + str(bookId)
                + "/"
                + str(self.chapter)
                + "/"
                + str(count)
                + "/"
            )

            try:
                req = requests.get(verse_url, timeout=60).text
                reqDic = json.loads(req)
            except Exception as e:
                print(f"Failed to load data: {e}")
                return 

            bookText = reqDic["text"].strip()
            text_no_s = re.sub(r"<S>.*?</S>", "", bookText, flags=re.DOTALL | re.IGNORECASE)
            cleaned_text = bleach.clean(text_no_s, tags=[], strip=True)
            # Len Check to make sure the block isn't larger than discord allows.
            if len(verse_block) + len(bookText) >=1800:
                verse_block += "... (truncated)"
                break 
            else:
                verse_block += cleaned_text + "\n"

            count += 1
            
 
       
        return f"{self.book} {self.chapter}:{self.verse_start}-{self.verse_end} \n\n{verse_block}"


