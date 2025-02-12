import sys

# To import files from directories
from library.scramble.documents import *
from library.scramble.contentanalysis import *


if __name__ == "__main__":
    # Show options to proceed on load
    print("Starting astraea. Type 'help' for a list of commands")
    print('')

    # Load existing data file
    command = ""
    filepath = ""
    file = ""

    docs = Documents()
    
    while True:
        command = input()
        match command:
            
            case "help":
                print('')
                print('     new         Create a new data file')
                print('     load        Load an existing data file')
                print('')
                print('     show        Show existing documents')
                print('     inspect     Show the content of a single document')
                print('     add         Add a document to the data file')
                print('')
                print('     save        Saves changes to current file')
                print('     quit        Quit astrea')
                print('')

            case "new":
                print('')
                print('Please provide the file path where to save the file (relative to this file)')
                print('')
                filepath = input()
                file = open(filepath + ".json", "x")

            case "load":
                print('')
                print('Please provide the file path to load (relative to this file)')
                print('')
                filepath = input()
                file = open(filepath, "w")
                print('\nFile loaded\n')
            
            case "add":
                name = input("Document name: ")
                content = []
                print("Input content: Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
                while True:
                    try:
                        line = input()
                    except EOFError:
                        break
                    content.append(line)
                docs.entries.append(Document(name, content, None))
                print('\nContent added\n')

            case "save":
                with open(filepath, "w") as file:
                    json.dump([ob.__dict__ for ob in docs.entries], file)

            case "quit":
                print('')
                print("Goodbye!")
                sys.exit()

            case _:
                print("Command not recognised")

    # Add documents