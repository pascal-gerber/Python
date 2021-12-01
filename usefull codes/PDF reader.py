#Import the required Libraries
import PyPDF2
from tkinter import *
from tkinter import filedialog
#Create an instance of tkinter frame
win= Tk()
#Set the Geometry
#Create a Text Box
text= Text(win,width= 200,height=100)
text.pack(pady=20)
#Define a function to clear the text
def clear_text():
   text.delete(1.0, END)
#Define a function to open the pdf file
def open_pdf():
   file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      #Open the PDF File
      pdf_file= PyPDF2.PdfFileReader(file)
      #Select a Page to read
      page = ""
      for each in range(pdf_file.getNumPages()):
         page = pdf_file.getPage(each)
         content=page.extractText()
         text.insert(INSERT,str(content) + "page " + str(each + 1) + "\n---------------------------------------------------------------------------------------------------------------\n\n")

      

#Define function to Quit the window
def quit_app():
   win.destroy()
#Create a Menu
my_menu= Menu(win)
win.config(menu=my_menu)
#Add dropdown to the Menus
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu= file_menu)
file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_command(label="Clear",command=clear_text)
file_menu.add_command(label="Quit",command=quit_app)
win.geometry("2000x1000")
win.mainloop()
