from tkinter import Tk, Canvas,Frame
import gui, gui1, gui2, gui3

class APP(Tk):
  def __init__(self,*args,**kwargs):
    Tk.__init__(self,*args,**kwargs)
    self.title("Example-multiple-GUI")
    
    container = Frame(self)
    container.pack(side="top",fill="both",expand = True)
    container.grid_rowconfigure(0,weight=1)
    container.grid_columnconfigure(0,weight=1)

    self.frames = {}

    for F in(gui, gui1, gui2, gui3):
      frame = F(container,self)
      self.frames[F] = frame
      frame.grid(row=0,column=0,sticky="nsew")
    
    self.showframe(gui)

  def show_frame(self,cont):
    if hasattr(self,"current_frame"):
      self.current_frame.destroy()
    frame = self.frames[cont]
    frame.tkraise()