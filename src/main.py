# To import files from directories
from pathlib import Path
import os
import sys

# To import files from directories
from library.scramble.documents import *
from library.scramble.contentanalysis import *

if __name__ == "__main__":
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/externaldata-csvs/job_skills.csv'))
        files = Documents()
        files.addFromCSVFile(filename, "job_skills")

        wordcounter = ContentAnalysis()
        wordcounter.settings.IncludeChars.append("+")
        wordcounter.settings.MaxWordsInPhrase = 5
        wordcounter.addDocuments(files)

        wordcounter.printOrdered()

        THIS_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        Result_Location = os.path.join(THIS_FOLDER, 'outputs/')
        wordcounter.saveToFile(Result_Location, 'results.txt')