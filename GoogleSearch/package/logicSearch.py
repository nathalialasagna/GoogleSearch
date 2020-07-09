
from googlesearch import search


def googleSearch(searchWords,updateProgressBar):
    maxProgressBar =0
    nuberOfLinks = 10
    timeBreak = 2
    
    global links, searchWordsresult
    searchWordsresult =[]  
    links=[]

    for searchWord in searchWords:

        maxProgressBar += 20
 
        
        for link in search(searchWord, tbs="qdr:Y", num=nuberOfLinks,stop=nuberOfLinks,pause=timeBreak):
            links +=[link]
            searchWordsresult +=[searchWord]

        updateProgressBar(maxProgressBar)
                

