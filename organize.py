from os import listdir, startfile
from os.path import isfile, join
from commonUtils import *
from constants import Unknown, MISC


def organize(folderName):
    for file in listdir(folderName):
        if isfile(join(folderName, file)):
            fileExtension = getFileExtension(file)
            path = ''
            if fileExtension != Unknown:
                fileType = fileExtension['type']
                fileDescription = fileExtension['description']
                if(isCommonFile(fileType)):
                    path = join(folderName, fileType)
                else:
                    path = join(folderName, fileType, fileDescription)
            else:
                path = join(folderName, MISC)

            createFolder(path)
            moveFile(join(folderName, file), join(path, file))


def main():
    folderName = chooseFolder()
    organize(folderName)
    startfile(folderName)


if __name__ == '__main__':
    main()
