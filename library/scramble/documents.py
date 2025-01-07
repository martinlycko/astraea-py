# To import files from directories
from pathlib import Path
import os

# For testing
import unittest


class Document:
    
    def __init__(self, text, attributes):
        self.text = text
        self.attributes = attributes


class Documents:

    def __init__(self):
        self.entries = []

    def addFromDirectory(self, path):
        files = Path(path).glob('*')
        for file in files:
            self.addFromFile(file)

    def addFromFile(self, filepath):
        with open(filepath, 'r') as file:
            self.entries.append(Document(file.readlines(), None))


class TestDocuments(unittest.TestCase):
    def test_FileImport(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'testdata', 'test-data4.txt')

        files = Documents()
        files.addFromFile(filename)

        self.assertEqual(files.entries[0].text[0], "test test test\n")

if __name__ == '__main__':
    unittest.main()