from tkinter import *
from tkinter.ttk import *
from Translate import translate


class App(Frame): # calling a bunch of classes in the main app frame
    
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.msg = Message(master, width=600, text="Please enter your python line of code to analyse.", pady=10,
                           padx=10)
        self.msg.config(font=('times', 16, 'italic'))
        self.msg.pack()      
        self.form = Form(self)
        self.form.pack()
        self.sep = Separator(orient=HORIZONTAL)
        self.sep.pack()
        self.outbox = Output(self)
        self.outbox.pack()
        self.answerLabels = answerLabels(self)
        self.answerLabels.pack(side=TOP)
        self.userOutput = answerbox(self)
        self.userOutput.pack()


class Form(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.input = Text(self, height=1, wrap=NONE, pady=10, padx=10) 
        self.input.bind('<Return>', self.exectute_code) #bind user input to return and reads it
        self.input.pack()
        self.button = Button(self, text="Read", command=self.exectute_code) #button reads user input
        self.button.bind('<Return>', self.exectute_code)
        self.button.pack(side=LEFT)
        self.clr = Button(self, text="Clear", command = self.clearbox)#clear button
        self.clr.pack(side=RIGHT)
               
    def clearbox(self): #clears the text field
        self.input.delete('1.0', 'end')
        self.master.userOutput.updateCode("")
 
    def exectute_code(self, event = None): #read and update return statement from input
        inputtext = self.input.get("1.0", '2.0')
        tClass = translate()
        self.master.userOutput.updateCode(tClass.pythontoenglish("print('hi', 'test')"))
        out = tClass.getRestList()
        try:
            lis = []
            word = ''
            flag = False
            for i in out:
                for c in i:
                    if c == ')':
                        continue
                    elif c == '"' or c == "'":
                        flag = True
                        continue
                    elif c is not '' and c is not ' ':
                        word += c
                if word is not '' or word is not ' ':
                    lis.append(word)
                    word = ''
            self.master.userOutput.updateSoln(lis)
        except:
            self.master.userOutput.updateSoln("This expression can't be evaluated.")
        return "break"
        
            
class Output(Frame): #returns user input under the 'output' frame 
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.outboxFrame = LabelFrame(self, text="Output", labelanchor="n")
        self.outboxFrame.pack()
        self.s = Label(self.outboxFrame, width=125)
        self.s.pack()

    def updateoutput(self, outputtext): #update output
        self.outputtext.set(outputtext)
    
    def Enterkey(self, outputtext): #create enter key shorcut
        self.outputtext.set(outputtext)



class answerLabels(Frame): #Labels for the answers
    def __init__(self, master, **kw):
        super().__init__(master, **kw)   
        self.label1 = Label(self, text="Computer Code\t\t\t\t\t\t\tAnswer")
        self.label1.pack()


class answerbox(Frame): #The user answer in terms of code and evaluated answer is printed here
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.LeftTextbox = Text(self, width = 45, height = 15) #create left textbox (code output)
        self.LeftTextbox.pack(side=LEFT)
        self.RightTextbox = Text(self, width = 45, height = 15) #create right textbox (evaluated output0
        self.RightTextbox.pack(side=RIGHT)

    def updateCode(self, text):
        self.LeftTextbox.delete("0.0", "end")
        self.LeftTextbox.insert("0.0", text)

    def updateSoln(self, text):
        #self.RightTextbox.delete("0.0", "end")
        self.RightTextbox.insert("0.0", text)

        
