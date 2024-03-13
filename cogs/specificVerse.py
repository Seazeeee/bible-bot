import requests
import json
import difflib

class specificVerse():


    def __init__(self, book: str, chapter: int, verse: int, translation = None):

        english_translations_dict = {
        "YLT", "KJV", "NKJV", "WEB", "RSV", "CJB", "TS2009", "LXXE", "TLV", "LSB", "NASB", "ESV", "GNV", "DRB", 
        "NIV2011", "NIV", "NLT", "NRSVCE", "NET", "NJB1985", "SPE", "LBP", "AMP", "MSG", "LSV", "BSB"}


        self.book = book
        self.chapter = chapter
        self.verse = verse
        
        if translation == None or translation not in english_translations_dict:
            self.translation = "ESV"
        else:
            self.translation = translation
    
    def pullVerse(self):


        # Has to have a capital name "Genesis"
        # Has to match spaces

        library = {
        1: "Genesis", 2: "Exodus", 3: "Leviticus", 4: "Numbers", 5: "Deuteronomy",
        6: "Joshua", 7: "Judges", 8: "Ruth", 9: "1 Samuel", 10: "2 Samuel",
        11: "1 Kings", 12: "2 Kings", 13: "1 Chronicles", 14: "2 Chronicles",
        15: "Ezra", 16: "Nehemiah", 17: "Esther", 18: "Job", 19: "Psalm",
        20: "Proverbs", 21: "Ecclesiastes", 22: "Song of Solomon", 23: "Isaiah",
        24: "Jeremiah", 25: "Lamentations", 26: "Ezekiel", 27: "Daniel",
        28: "Hosea", 29: "Joel", 30: "Amos", 31: "Obadiah", 32: "Jonah",
        33: "Micah", 34: "Nahum", 35: "Habakkuk", 36: "Zephaniah", 37: "Haggai",
        38: "Zechariah", 39: "Malachi", 40: "Matthew", 41: "Mark", 42: "Luke",
        43: "John", 44: "Acts", 45: "Romans", 46: "1 Corinthians", 47: "2 Corinthians",
        48: "Galatians", 49: "Ephesians", 50: "Philippians", 51: "Colossians",
        52: "1 Thessalonians", 53: "2 Thessalonians", 54: "1 Timothy", 55: "2 Timothy",
        56: "Titus", 57: "Philemon", 58: "Hebrews", 59: "James", 60: "1 Peter",
        61: "2 Peter", 62: "1 John", 63: "2 John", 64: "3 John", 65: "Jude",
        66: "Revelation"
        }

        for key, value in library.items():
            if value == self.book:
                exact_match = key
                break
            else:
                close_matches = difflib.get_close_matches(self.book, library.values(), n=1)
                if close_matches:
                    close_match_title = close_matches[0]
                    for key, value in library.items():
                        if value == close_match_title:
                            exact_match = key
                            break
        
        bookId = exact_match
        # https://bolls.life/get-verse/<slug:translation>/<int:book>/<int:chapter>/<int:verse>/

        url = "https://bolls.life/get-verse/"+ str(self.translation) + "/" + str(bookId) + "/" + str(self.chapter) + "/" + str(self.verse) + "/"
        verse_url = "https://bolls.life/"+ str(self.translation) + "/" + str(bookId) + "/" + str(self.chapter) + "/" + str(self.verse) + "/"

        req = requests.get(url).text

        # turn text into dictionary
        
        reqDic = json.loads(req)

        # Grab required index's

        bookText = reqDic["text"]

        return f'{self.book} {self.chapter}:{self.verse} \n\n{bookText} \n {verse_url}'


    

    