import os
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""


# class FileManager:
def createFile(fileName):
    try:
        open(fileName, "x")
    except:
        return "File already exists"

def readFile(fileName):
    try:
        return (open(fileName, "r").read())
    except:
        return "File doesn't exists"

def writeFile(fileName, text):
    try:
        open(fileName, "w").write(text)
    except:
        return "File doesn't exists"

def appendFile(fileName, text):
    try:
        open(fileName, "a").write(text)
    except:
        return "File doesn't exists"

def clearFile(fileName):
    try:
        open(fileName, "w").write("")
    except:
        return "File doesn't exists"

def deleteFile(fileName):
    try:
        os.remove(fileName)
    except:
        return "File doesn't exists"
