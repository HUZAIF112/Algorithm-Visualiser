from tkinter import *
from tkinter import ttk
import random


root = Tk() 
root.title('Algorith visualiser')
root.maxsize(1000,700)
root.configure(bg='silver')

    

            


     



   
    
def generate():
      global data

      data = []
      for i in range(0, 100):
        random_value = random.randint(1,150)
        data.append(random_value)

      drawData(data, ['#ffd700' for x in range(len(data))])
  


def drawData(data,colour_this):
    canvas.delete('all')
    canvas_height = 400  
    canvas_width = 800
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 290
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colour_this[i])

    root.update_idletasks

    














User_interface = Frame(root, width= 900, height=500 )
User_interface.grid(row=0 ,column=0, padx=15, pady= 10 )


B1 = Button(User_interface,text='sort')
B1.grid(row=0,column=1,padx=10,pady=5)

B2= Button(User_interface,text='Generate', command= generate)
B2.grid(row=0,column=2,padx=10,pady=10)

canvas = Canvas(root,width=800,height=400)
canvas.grid(row=3,column=0)
canvas.configure(bg='#000000')




root.mainloop()
