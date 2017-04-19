# Name:  Debbie Yung
# Student Number:  10417380


# Import the required modules.
import tkinter
import tkinter.messagebox
import json



class ProgramGUI:

    def __init__(self):
        self.main = tkinter.Tk()

        #Window Attributes
        self.main.title('Joke Bot')
        self.main.geometry('700x300')      
        self.main.wm_resizable(0,0)
        self.main.wm_iconbitmap(bitmap = 'Custom-Icon-Design-Flatastic-10-Bear.ico')
        self.main.config(bg='Dark Orange')
        self.setupFrame = tkinter.Frame(self.main, bg='Dark Orange')
        self.submitFrame = tkinter.Frame(self.main, bg='Dark Orange')
        
        #Get file 
        self.filename = 'data.txt'
        try:
            f = open('data.txt','r')
            data = json.load(f)
            f.close()
        except FileNotFoundError: 
            tkinter.messagebox.showerror('Error', 'No Jokes stored. Program will now exit.')
            self.main.destroy()
            return

        self.dataList = data
        
        #Set current joke count
        self.currentJoke = 0
        
        #Empty labels to populate
        self.setupLabel = tkinter.Label(self.setupFrame, text='Setup Placeholder')
        self.setupLabel.config(font=('helvetica', 15, 'bold'))
        self.setupLabel.pack(pady=(20,10))

        self.punchlineLabel = tkinter.Label(self.setupFrame, text='__________')
        self.punchlineLabel.config(font=('helvetica', 15, 'italic'), wraplength=550)
        self.punchlineLabel.pack(pady=(30,80))

        self.RatingLabel = tkinter.Label(self.setupFrame, text="Rating Placeholder")
        self.RatingLabel.pack()

        tkinter.Label(self.submitFrame, text='Your rating:').pack(side='left', pady=(5,0))
        self.entry = tkinter.Entry(self.submitFrame, width=5)
        self.entry.pack(side='left', padx=(5,0), pady=(5,0))
        self.entry.focus_set()
        self.subButton = tkinter.Button(self.submitFrame, text='Submit', command=self.rateJoke)
        self.subButton.pack(padx=(5,6),pady=(5,0))
        self.subButton["state"] = "disabled"

        #Load first joke
        self.showJoke()

        #Pack Frames
        self.setupFrame.pack()
        self.submitFrame.pack()
            
     
        tkinter.mainloop()



    def showJoke(self):
        #Set dictionary joke data as variables
        self.currentSetup = self.dataList[self.currentJoke]['setup']
        self.currentPunchline = self.dataList[self.currentJoke]['punchline']
        self.numRate = self.dataList[self.currentJoke]['numOfRatings']
        self.sumRate = self.dataList[self.currentJoke]['sumOfRatings']
        
        #Display joke data by changing Label configs
        if self.numRate == 0:           
            self.setupLabel.config(text=self.currentSetup)
            self.punchlineLabel.after(3500, self.showPunch)
            self.RatingLabel.config(text="Rated 0 times.")
            tkinter.messagebox.showinfo('Info', 'Joke has not been rated yet.')
            
        else:
            self.setupLabel.config(text=self.currentSetup)
            self.punchlineLabel.after(3500, self.showPunch)
            self.avgRate = round(int(self.sumRate)/int(self.numRate),1)
            self.RatingStr = "Rated {} time(s). Average rating is {}/5.".format(self.numRate, self.avgRate)
            self.RatingLabel.config(text=self.RatingStr)


                    
    #Delay showing punchline and button activity
    def showPunch(self):
        self.punchlineLabel.config(text=self.currentPunchline)
        self.subButton["state"] = "active"        



    def rateJoke(self):
        
        if not self.entry.get():
            tkinter.messagebox.showerror('Rating Error','Empty Field.\nPlease enter a number to rate.')

        try:
            if int(self.entry.get()) in range(1,6): 
                #Update Rating for dataList
                self.dataList[self.currentJoke]['numOfRatings'] = self.dataList[self.currentJoke]['numOfRatings'] + 1
                self.dataList[self.currentJoke]['sumOfRatings'] = self.dataList[self.currentJoke]['sumOfRatings'] + int(self.entry.get())
         
                #Write/Save Rating
                f = open('data.txt', 'w')
                json.dump(self.dataList, f, indent = 4)
                f.close()

                #Show next or last joke
                self.actualLen = len(self.dataList) - 1
                
                if self.currentJoke < self.actualLen:
                    tkinter.messagebox.showinfo('Rating Recorded','Thank you for rating.\nThe next joke will now appear.')
                    self.currentJoke +=1
                    self.punchlineLabel.config(text='__________')
                    self.showJoke()
                    self.entry.delete(0,'end') #http://stackoverflow.com/questions/2260235/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter
                    self.subButton["state"] = "disabled"
                elif self.currentJoke == self.actualLen: 
                    tkinter.messagebox.showinfo('Rating Recorded','Thank you for rating.\nThat was the last joke.\nThe program will now end.')
                    self.punchlineLabel.config(text='__________')
                    self.subButton["state"] = "disabled"
                    self.main.destroy()
                    
            else:
                tkinter.messagebox.showerror('Rating Error','Invalid entry.\nPlease enter a number between 1 and 5')
        except ValueError:
            tkinter.messagebox.showerror('Rating Error','Invalid entry.\nNot a number.\nPlease enter a number.')




# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
