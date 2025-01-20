# ToDos
# Need better testing for the different settings
# Need to seperate test cases into each test document
# Need a function that returns a count given a key catching the error if key not present
# Update save to file functionality

# To import files from directories
from pathlib import Path
import os
import json

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
        cleanedText = "".join(char for char in text if char.isalnum() or char == " " or char in self.settings.IncludeChars)
        
        if self.settings.CaseSensitive == False:
            cleanedText = cleanedText.lower()
        
        return cleanedText

    def getPhrases(self, text):
        phrases = []

        last_words = []
        for word in text.split():
            if len(word) <= self.settings.MaxWordLength and word not in self.settings.ExcludeWordsOnImport:
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

    def getCount(self, phrase):
        if self.settings.CaseSensitive == False:
            self.entries['lorem']
        else:
            pass # Add functioanlity for case sensitive
    
    def printOrdered(self, by="Count", reverse=True):
        if by == "Count":
            for key, value in sorted(self.entries.items(), key=lambda phrase: phrase[1], reverse=reverse): 
                print("{}: {}".format(key, value))
        else:
            if by == "Items":
                for key, value in sorted(self.entries.items(), key=lambda phrase: phrase[0], reverse=reverse): 
                    print("{}: {}".format(key, value))
            else:
                print("Incosistent print")

    def saveToFile(self, path, filename):
        file = open(path+filename, "w")
        for k, v in sorted(self.entries.items(), key=lambda phrase: phrase[1], reverse=True):
            file.write(str(k) + ': '+ str(v) + '\n')
        file.close()

class ContentAnalysisSettings():
    
    def __init__(self):
        self.CaseSensitive = False
        self.MaxWordLength = 32
        self.MaxWordsInPhrase = 1
        self.IncludeChars = ["(", ")", "/", "'"]
        self.ExcludeWordsOnImport = stopwords
        self.synonyms = []

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 
'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 
'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 
'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are',
 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing',
 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 
'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 
'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 
'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 
'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y',
 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 
'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',
 "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 
'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

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