# To import files from directories
from pathlib import Path
import os
import sys

# To import files from directories
from library.scramble.documents import *
from library.scramble.contentanalysis import *

if __name__ == "__main__":
        dirname = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
        files = Documents()
        files.addFromDirectory(dirname)

        wordcounter = ContentAnalysis()
        wordcounter.settings.IncludeChars.append("+")
        wordcounter.addDocuments(files)

        wordcounter.printOrdered()