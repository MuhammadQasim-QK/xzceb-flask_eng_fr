''' THIS PROGRAM TRANSLATER LANGUAGES'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

def __english_to_french__(english_text):
    french_text = language_translator.translate(
    english_text,
    model_id = 'en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    return french_text

def __french_to_english__(french_text):
    english_text = language_translator.translate(
    french_text,
    model_id = 'fr-en').get_result()
    english_text = english_text['translations'][0]['translation']
    return english_text
      