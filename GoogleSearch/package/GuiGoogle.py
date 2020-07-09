from tkinter import *
from tkinter import messagebox,ttk,filedialog
from PIL import ImageTk, Image
import threading
import urllib
from package import rwFiles
from package import logicSearch




class GoogleSearchInterface():


    def __init__(self, master):
        self.master = master
        master.geometry('500x300')

        self.magnifyingLogo = ImageTk.PhotoImage(Image.open(r'logo\magnifying.png').resize((50,50), Image.ANTIALIAS))
        self.labelMagnifyingLogo = Label(image=self.magnifyingLogo)
        self.labelMagnifyingLogo.grid(row=0,column=0, padx=0, pady=20)
                
        self.icon = PhotoImage(file = r"logo\folder.png") 
        self.iconDirectory = self.icon.subsample(1, 1) 

        self.FileLabel = Label(master, text = 'Search File:')
        self.FileLabel.grid(row=1,column=0,padx=5)

        self.fileEntry = Entry(master, width=50)
        self.fileEntry.grid(row=1,column=1,columnspan=2)

        self.fileButton = Button(master, image=self.iconDirectory,command=self.openFile)
        self.fileButton.grid(row=1,column=3,padx=10)

        self.DestinyDirectoryLabel = Label(master, text = 'Destiny Folder:')
        self.DestinyDirectoryLabel.grid(row=2,column=0)

        self.DestinyDirectoryEntry= Entry(master, width=50)
        self.DestinyDirectoryEntry.grid(row=2,column=1, pady=20,columnspan=2)

        self.directoryButton = Button(master, image=self.iconDirectory,command=self.openFolder)
        self.directoryButton.grid(row=2,column=3,padx=10, pady=20)

        self.FileNameEntry = Label(master, text = 'File Name:')
        self.FileNameEntry.grid(row=3,column=0)

        self.FileNameEntry = Entry(master, width=23)
        self.FileNameEntry.grid(row=3,column=1, pady=10)

        self.searchButton = Button(master, text = 'Search',padx=50,command=lambda : self.runThread(self.GoogleSearch,self.fileEntry.get(),self.DestinyDirectoryEntry.get(),self.FileNameEntry.get()))
        self.searchButton.grid(row=5,column=1,padx=10,pady=20)

        self.closeButton = Button(master, text = 'Close',padx=50,command=self.quit)
        self.closeButton.grid(row=5,column=2,padx=10,pady=20)

    def runThread(self,func,args,args2,args3):
        self.th = threading.Thread(target=func, args=(args,args2,args3))
        self.th.start()
    
    def openFolder(self):
        self.DestinyDirectoryEntry.delete(0, END)
        self.master.directory = filedialog.askdirectory(title='Select a directory')
        self.DestinyDirectoryEntry.insert(0,self.master.directory )

    def openFile(self):
        self.fileEntry.delete(0, END)
        self.master.filename = filedialog.askopenfilename(title='Select a file', filetypes=(('xlsx files','*.xlsx'),('all files','*.*')))
        self.fileEntry.insert(0,self.master.filename)


    def quit(self):
        sys.exit()

    def updateProgressBar(self,maxProgressBar):

        self.progress.config(mode='determinate',maximum=len(rwFiles.searchWords)*20,value=maxProgressBar)

        
    def GoogleSearch(self,fileEntry,DestinyDirectoryEntry,FileNameEntry):
        
        self.master.geometry('500x350')
        
        self.progress=ttk.Progressbar(self.master,orient=HORIZONTAL,length=300) 
        self.progress.grid(row=4,column=1,pady=10,columnspan=2)
       
        try:
            rwFiles.readFile(fileEntry)

        except:

            self.responseFileRead = messagebox.showerror('ERROR', 'Error in read file')
            Label(self.master, text=self.responseFileRead)
    
        if any(rwFiles.searchWords) == True:

            try:

                logicSearch.googleSearch(rwFiles.searchWords,self.updateProgressBar)
                rwFiles.searchResult(logicSearch.searchWordsresult, logicSearch.links,DestinyDirectoryEntry,FileNameEntry)
                self.responseGoogleProcess = messagebox.showinfo('Completed','Completed')
                Label(self.master, text=self.responseGoogleProcess)

            except urllib.error.HTTPError:

               self.responseGoogleProcess = messagebox.showerror('ERROR', 'Too many requests, please try later.')
               Label(self.master, text=self.responseGoogleProcess)
               
               if any(logicSearch.links) == True:

                    rwFiles.searchResult(logicSearch.searchWordsresult, logicSearch.links,DestinyDirectoryEntry,FileNameEntry)
        else:

            self.responseGoogleProcess = messagebox.showerror('ERROR', 'The file is empty')
            Label(self.master, text=self.responseGoogleProcess)
        
    
 





