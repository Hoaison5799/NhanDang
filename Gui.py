from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import Tk, RIGHT, BOTH, RAISED, TOP, LEFT, X, N, Text, W, E, filedialog, Canvas, NW, messagebox, INSERT, END
from tkinter.ttk import Frame, Button, Style, Label, Entry
import Main
import cv2


class CanvasButton():
   def __init__(self, canvas):
        def Show():
            text= self.TextBrowser.get("1.0", "end-1c")
            self.img = Image.open(text)
            photo = ImageTk.PhotoImage(self.img)
            label = Label(canvas, image=photo)
            label.image = photo
            label.place(x=250, y=120)

        def ShowA(event):
            Show()
            Work()
            return 'break'

        def Work():
            text = self.TextBrowser.get("1.0", "end-1c")
            photo = cv2.imread(text)
            BienSo = Main.Find(photo)
            fontStyle = tkFont.Font(family="Helvetica", size=20, weight="bold")
            lable1 = Label(canvas, text=BienSo, font=fontStyle)
            self.KQ = canvas.create_window(120, 170, width=170, height=50, window=lable1)

        def Browse():
            Tam = filedialog.askopenfilename(initialdir="*/", title="Select Picture",
                                                  filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"),
                                                             ("all files", "*.*")))
            if Tam=="": return
            self.TextBrowser.delete('1.0',END)
            self.TextBrowser.insert(INSERT, str(Tam))
            Show()


        self.img = None
        self.canvas = canvas

        fontStyle = tkFont.Font(family="Helvetica", size=36, weight="bold")
        self.lable = Label(canvas, text= "Biển số xe", font=fontStyle)
        self.TieuDe = canvas.create_window(600, 30, width=500, height=50, window=self.lable)

        self.buttonBrowser = Button(canvas, text="Browser", command=Browse)
        self.id = canvas.create_window(70, 90, width=100, height=30,
                                       window=self.buttonBrowser)

        self.TextBrowser = Text(canvas, font="Arial 15")
        self.id2 = self.canvas.create_window(600, 90, width=700, height=30,
                                             window=self.TextBrowser)
        self.TextBrowser.bind('<Return>', ShowA)

        self.buttonWork = Button(canvas, text="Identified", command=Work)
        self.id3 = canvas.create_window(70, 130, width=100, height=30,
                                       window=self.buttonWork)





root=Tk()
root.title("nhom 17")
root.wm_geometry("1000x900")

canvas = Canvas(root,width = 1920, height= 1080)
canvas.place(x=0,y=0)

CanvasButton(canvas)

#root.geometry("1000x700+1+1")
#app = Example(root)
root.mainloop()


