import unittest
from translator import __english_to_french__, __french_to_english__

class TestMyTranslator(unittest.TestCase):

#Equality
    def test___english_to_french__(self):
        self.assertEqual(__english_to_french__("Hello"),"Bonjour")

    def test___french_to_english__(self):
        self.assertEqual(__french_to_english__("Bonjour"),"Hello")    
#Un-Equality 
    def test___english_to_french__(self):
        self.assertNotEqual(__english_to_french__("Hello"),"Hello")
    #Bonjour To Hello test for french to english
    def test___french_to_english__(self):
        self.assertNotEqual(__french_to_english__("Bonjour"),"Bonjour")
if __name__ == '__main__':
    unittest.main()