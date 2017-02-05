from components.app import *

root = Tk()
root.title(string="Py (QHacks 2017)")
root.iconbitmap("favicon.ico")
root.minsize(width=500, height=500)
root.resizable(width=False, height=False)
app = App(root)
app.pack()
root.mainloop()
