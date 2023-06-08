import os
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""


class FileManager:
    def __init__(self, fileName=""):
        self.fileName = fileName
    
    def create(self):
        """ Create the file """
        with open(self.fileName, "w") as file:
            file.write("")

    def read(self):
        """ Read the file """
        with open(self.fileName, "r") as file:
            return file.read()

    def write(self, text):
        """ Erase the previous text and write new text """
        with open(self.fileName, "w") as file:
            file.write(text)

    def append(self, text):
        """ Adds text to the file """
        with open(self.fileName, "a") as file:
            file.write(text)
    
    def clear(self):
        """ Remove all text in the file """
        with open(self.fileName, "w") as file:
            file.write("")

    def delete(self):
        """ Delete the file """
        os.remove(self.fileName)
