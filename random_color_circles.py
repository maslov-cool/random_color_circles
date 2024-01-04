import tkinter
from random import uniform as un


def draw(event):
    random_x_0 = un(0, 600)
    random_y_0 = un(0, 600)
    d = un(1, 200)
    r, g, b = un(0, 256), un(0, 256), un(0, 256)
    r, g, b = [hex(int(i))[2:] if i != '0' else '00' for i in [r, g, b]]
    canvas.create_oval(random_x_0, random_y_0, random_x_0 + d, random_y_0 + d, fill='#' + ''.join([r, g, b]))
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
