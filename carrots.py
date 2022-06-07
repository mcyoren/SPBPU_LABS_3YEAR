import pygame
from pygame.locals import *
from tkinter import *

import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

RED = (255, 0, 0)
GRAY = (150, 150, 150)


root = Tk()
root.title("Labs: Carrots")

width = 500
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
global scale_mic
scale_mic = 0.7
window_size = int(screen_width / 2)

pygame.init()

img_micro = pygame.image.load(resource_path("micro.png"))
img_micro = pygame.transform.scale(img_micro, (window_size, window_size))
rect_micro = img_micro.get_rect()
rect_micro.center = window_size // 2, window_size // 2

def SetMicro(scale):
    global scale_mic
    scale_mic = scale


def LoadImage(path):
    img = pygame.image.load(resource_path(path))
    Pygame_Go(img)

def Pygame_Go(img):
    screen = pygame.display.set_mode((window_size, window_size))
    running = True
    img.convert_alpha()

    x = 8770
    y = 4360
    cell_size = 200 * scale_mic
    step = 5 * scale_mic
    rmax = 9000 - cell_size

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        if event.type == KEYDOWN:
            if event.key == K_UP:
                y = y - step if step < y else 0
            elif event.key == K_DOWN:
                y = y + step if step + y < rmax else rmax
            elif event.key == K_LEFT:
                x = x - step if step < x else 0
            elif event.key == K_RIGHT:
                x = x + step if step + x < rmax else rmax
            elif event.key == K_z:
                if cell_size > 100:
                    cell_size = cell_size / 1.05
                    step = step / 1.05
            elif event.key == K_x:
                if cell_size < 2000:
                    cell_size = cell_size * 1.05
                    step = step * 1.05

        zoom = window_size / cell_size + 1
        rect = pygame.Rect((x, y, cell_size, cell_size))
        image = pygame.Surface(rect.size).convert()
        image.blit(img, (0, 0), rect)
        image = pygame.transform.rotozoom(image, 0, zoom)
        screen.blit(image, pygame.Rect((0, 0, window_size, window_size)))
        screen.blit(img_micro, rect_micro)
        pygame.display.update()

    pygame.quit()
#================================FRAMES=========================================
Top = Frame(root, width=600, bd=1, relief=SOLID)
Top.pack(side=TOP)
But0 = Frame(root, width=50, height=50, bd=1, relief=SOLID)
But0.pack(side=BOTTOM)
But0.pack(padx=140)
But0.pack(pady=10)
But1 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But1.pack(side=LEFT)
But1.pack(padx=40)
But1.pack(pady=10)
But2 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But2.pack(side=LEFT)
But2.pack(padx=20)
But2.pack(pady=10)
But3 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But3.pack(side=LEFT)
But3.pack(padx=20)
But3.pack(pady=10)
But4 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But4.pack(side=LEFT)
But4.pack(padx=20)
But4.pack(pady=10)


#================================LABEL WIDGETS==================================
#================================LABEL WIDGETS==================================
lbl_title = Label(Top, text="KoronaLab", width=600, font=("arial", 20))
lbl_title.pack(fill=X)
lbl_text0 = Label(But0, text="LOOK", font=("arial", 30))
lbl_text0.bind("<Button-1>", lambda _: LoadImage("carrots.png"))
lbl_text0.pack()
lbl_text1 = Label(But1, text="Mic1", font=("arial", 20))
lbl_text1.bind("<Button-1>", lambda _: SetMicro(0.7))
lbl_text1.pack()
lbl_text2 = Label(But2, text="Mic2", font=("arial", 20))
lbl_text2.bind("<Button-1>", lambda _: SetMicro(1.5))
lbl_text2.pack()
lbl_text3 = Label(But3, text="Mic3", font=("arial", 20))
lbl_text3.bind("<Button-1>", lambda _: SetMicro(0.95))
lbl_text3.pack()
lbl_text4 = Label(But4, text="Mic4", font=("arial", 20))
lbl_text4.bind("<Button-1>", lambda _: SetMicro(1.2))
lbl_text4.pack()


#================================INITIALIZATION=================================
if __name__ == '__main__':
    root.mainloop()