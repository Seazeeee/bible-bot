import discord
import json
from utils.utils import openai_call
from .specificVerse import specificVerse

class question():

    def __init__(self, question: str):
        self.question = question

    def get_reponse_from_OpenAI(self):

        response = openai_call(self.question)

        return json.loads(response)

    def ask_question(self):
        
        ai_verse = self.get_reponse_from_OpenAI()
       
        return specificVerse(ai_verse["Book"], ai_verse["Chapter"],
                             ai_verse["Verse"]).pullVerse()

