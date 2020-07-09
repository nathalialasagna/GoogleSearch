
import pandas as pd
import os


def searchResult(searchWord, links,destinyDirectory,fileName):

    searchResult = pd.DataFrame({"Word":searchWord,"Url":links})
    destinyDirectory = destinyDirectory.replace('/','\\')
    searchResultFile = os.path.join(destinyDirectory, fileName +'.xlsx')

    writeSearchResultFile = pd.ExcelWriter(searchResultFile, engine='openpyxl',mode='w',options={'strings_to_urls': False})# pylint: disable=abstract-class-instantiated
    searchResult.to_excel(writeSearchResultFile)
    writeSearchResultFile.close()


def readFile(filePath):

    global searchWords
    fileData = pd.read_excel(filePath)
    searchWords = fileData['Words'].values.tolist()
 
