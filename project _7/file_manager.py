from datetime import datetime

class AllData:
    """Handles file writing, reading, searching and deleting."""
    
    def __init__(self, filename):
        self.filename = filename

    def AddEntry(self, text):
        with open(self.filename, "a") as file:
            file.write(text + "\n")
        print("Entry Added Successfully!")

    def ViewEntry(self):
        try:
            with open(self.filename, "r") as file:
                print("\nYour Journal Entries\n-------------------------")
                print(file.read())
        except FileNotFoundError:
            print("File not found.")

    def SearchEntry(self, keyword):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for linenum, line in enumerate(lines):
                    if keyword in line:
                        print(linenum, line)
        except FileNotFoundError:
            print("File not found.")

    def DeleteEntry(self):
        open(self.filename, "w").close()
        print("All entries deleted!")
