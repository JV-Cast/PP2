#OurPyPaint 4/21/2020

from tkinter import *

class PaintApp:
# Variables
    
     drawing_tool = "line"

     left_but = "up"

     x_pos, y_pos = None, None
     
     x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None
     
#Mouse Down

def left_but_down(self, event=None):
    self.left_but = "down"
        
    self.x1_line_pt = event.x
    self.y1_line_pt = event.y

#Mouse Up

    def left_but_up(self, event=None):
        self.left_but = "up"
        self.x_pos = None
        self.y_pos = None

        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawing_tool == "line":
            self.line_draw(event)

#Mouse Move

    def motion(self, event=None):
        if self.drawing_tool == "pencil":
            self.pencil_draw(event)

 

#Pencil

    def pencil_draw(self, event=None):

        if self.left_but == "down":

            if self.x_pos is not None and self.y_pos is not None:

                 event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE)
            
            self.x_pos = event.x
            self.y_pos = event.y


#Initialize

    def __int__(self, root):
        drawing_area = Canvas(root)

        drawing_area.pack()

        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

root = Tk()
paint_app = PaintApp(root)
root.mainloop()
