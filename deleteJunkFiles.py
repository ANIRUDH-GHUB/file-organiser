import os
from constants import junkFilePaths

def deleteJunkFiles(junkFilePaths):
    for filePath in junkFilePaths:
        
        fileList = os.listdir(filePath)
        folderSizeBeforeDeletion = len(fileList)
        undeletedFiles = 0
        
        for file in fileList:
            try:
                os.remove(filePath+"\\"+file)
            except:
                undeletedFiles += 1
                                
        fileList = os.listdir(filePath)
        folderSizeAfterDeletion = len(fileList)
        
        print("Successfully deleted ",folderSizeBeforeDeletion-folderSizeAfterDeletion ,"files from ",filePath)
        print("Failed to delete ",undeletedFiles,"file/files")         
    
#Example call showing temp file deletion by passing some junk folder paths
 
deleteJunkFiles(junkFilePaths)


