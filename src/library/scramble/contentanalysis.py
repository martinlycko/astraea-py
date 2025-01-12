# ToDos
# Need better testing for the different settings
# Need to seperate test cases into each test document
# Need a function that returns result in an asc/dec ordered
# Need a function that returns a count given a key catching the error if key not present

# To import files from directories
from pathlib import Path
import os

# For testing
import unittest

# Importing when main file is run
if __name__ != '__main__':
    import library.scramble.documents

class ContentAnalysis:

    def __init__(self):
        self.entries = {}
        self.settings = ContentAnalysisSettings()

    def addPhrase(self, phrase):
        self.entries[phrase] = self.entries.get(phrase, 0) + 1

    def addDocuments(self, documents):
        for entry in documents.entries:
            for line in entry.text:
                for phrase in self.getPhrases(self.cleanText(line)):
                        self.addPhrase(phrase)

    def cleanText(self, text):
        cleanedText = "".join(char for char in text if char.isalnum() or char == " ")
        
        if self.settings.CaseSensitive == False:
            cleanedText = cleanedText.lower()
        
        return cleanedText

    def getPhrases(self, text):
        phrases = []

        last_words = []
        for word in text.split():
            if len(word) <= self.settings.MaxWordLength:
                if self.settings.MaxWordsInPhrase == len(last_words):
                    last_words.pop(0)
                last_words.append(word)
                
                if self.settings.MaxWordsInPhrase == 1:
                    phrases.append(last_words[0])
                else: 
                    i = 0
                    while i < len(last_words):
                        if i == 0:
                            phrases.append(last_words[len(last_words)-1])
                        else:
                            phrases.append(" ".join(last_words[len(last_words)-i-1:len(last_words)+1]))
                        i = i + 1

        return phrases

class ContentAnalysisSettings():
    
    def __init__(self):
        self.CaseSensitive = False
        self.MaxWordLength = 32
        self.MaxWordsInPhrase = 2
        self.ExcludeWordsOnImport = []


class TestDocuments(unittest.TestCase):
    def test_sample1(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'testdata', 'test-data1.txt')

        files = documents.Documents()
        files.addFromFile(filename)

        wordcounter = ContentAnalysis()
        wordcounter.addDocuments(files)

        self.assertEqual(wordcounter.entries['lorem'], 1)
        # self.assertEqual(wordcounter.entries['Lorem'], 1)
        self.assertEqual(wordcounter.entries['ut'], 3)

    def test_sample2(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'testdata', 'test-data2.txt')

        files = documents.Documents()
        files.addFromFile(filename)

        wordcounter = ContentAnalysis()
        wordcounter.addDocuments(files)

        self.assertEqual(wordcounter.entries['test'], 3)
        # self.assertEqual(wordcounter.entries['Test'], 2)
        # self.assertEqual(wordcounter.entries['test1'], 0)

    def test_sample3(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'testdata', 'test-data3.txt')

        files = documents.Documents()
        files.addFromFile(filename)

        wordcounter = ContentAnalysis()
        wordcounter.addDocuments(files)

        self.assertEqual(wordcounter.entries['test1'], 1)
        self.assertEqual(wordcounter.entries['test2'], 1)
        self.assertEqual(wordcounter.entries['test3'], 1)
    
    def test_sample4(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'testdata', 'test-data4.txt')

        files = documents.Documents()
        files.addFromFile(filename)

        wordcounter = ContentAnalysis()
        wordcounter.addDocuments(files)

        self.assertEqual(wordcounter.entries['test'], 6)
        # self.assertEqual(wordcounter.entries['Test'], 6)
        # self.assertEqual(wordcounter.entries['test1'], 6)

if __name__ == '__main__':
    import documents
    unittest.main()