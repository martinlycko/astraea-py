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
                for word in line.lower().split():
                    self.addPhrase(word)


class ContentAnalysisSettings():
    
    def __init__(self):
        self.CaseSensitive = False
        self.ExcludeOnImport = []

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