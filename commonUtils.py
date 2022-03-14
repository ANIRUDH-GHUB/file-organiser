from os import makedirs
import shutil
from tkinter import filedialog
from tkinter import *
from constants import commonFiles, Unknown
import json

with open("assets/extensions.json") as f:
    extensions = json.load(f)


def chooseFolder():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected


def createFolder(folderName):
    try:
        makedirs(folderName)
    except FileExistsError:
        pass


def moveFile(source, destination):
    shutil.move(source, destination)


def isCommonFile(fileName):
    return fileName.lower() in commonFiles


def getFileExtension(fileName):
    fileType = ('.' + fileName.split(".")[-1]).upper()
    return extensions[fileType] if fileType in extensions else Unknown
