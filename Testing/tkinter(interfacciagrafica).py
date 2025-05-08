import tkinter
window = tkinter.Tk()
c = tkinter.Canvas(window)

def draw_oval(x1, y1, x2, y2, colour):
    if colour == None:
        c.create_oval(x1, y1, x2, y2)
    else:
        c.create_oval(x1, y1, x2, y2, fill=colour)
def draw_line(x1, y1, x2, y2):
    c.create_line(x1, y1, x2, y2)
def render_neutral_face():
# Draw face outline
    draw_oval(50, 50, 120, 120)
# Draw left eye
    draw_oval(60, 60, 80, 80)
    draw_oval(65, 65, 75, 75, 'black')
# Draw right eye
    draw_oval(90, 60, 110, 80)
    draw_oval(95, 65, 105, 75, 'black')
# Draw neutral mouth    
    draw_line(70, 110, 100, 110)

c.pack()
window.mainloop()