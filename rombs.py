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
root.title("Labs: Rombs")

width = 750
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
img_ruler = pygame.image.load(resource_path("ruler2.png"))
img_ruler = pygame.transform.scale(img_ruler, (window_size, window_size))
rect_ruler = img_ruler.get_rect()
rect_ruler.center = window_size // 2, window_size // 2

def SetMicro(N_mic):
    global scale_mic
    scale_mic = N_mic


def LoadImage0(event=None):
    global ruler_draw
    ruler_draw = True
    img0 = pygame.image.load(resource_path("mm_grid.png"))
    Pygame_Go(img0, True)


def LoadImage1(N_obr):
    global ruler_draw
    ruler_draw = False
    img0 = pygame.image.load(resource_path(f"rombs_{N_obr}.png"))
    Pygame_Go(img0, False)


def Pygame_Go(img, ruler_draw):
    screen = pygame.display.set_mode((window_size, window_size))
    running = True
    img.convert_alpha()
    img = pygame.transform.rotozoom(img, 0, scale_mic)
    rect = img.get_rect()
    rect.center = window_size // 2, window_size // 2

    moving = False

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    moving = True

            elif event.type == MOUSEBUTTONUP:
                moving = False

            elif event.type == MOUSEMOTION and moving:
                rect.move_ip(event.rel)

        angle = 0
        scale = 1
        if event.type == KEYDOWN:
            if event.key == K_s:
                if event.mod & KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1
                img = pygame.transform.rotozoom(img, angle, scale)
                rect = img.get_rect()
                rect.center = window_size // 2, window_size // 2

        screen.fill(GRAY)
        screen.blit(img, rect)
        if(ruler_draw):
            screen.blit(img_ruler, rect_ruler)
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
But2.pack(padx=30)
But2.pack(pady=10)
But3 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But3.pack(side=LEFT)
But3.pack(padx=30)
But3.pack(pady=10)
But4 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But4.pack(side=LEFT)
But4.pack(padx=30)
But4.pack(pady=10)
But5 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But5.pack(side=LEFT)
But5.pack(padx=30)
But5.pack(pady=10)
But6 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But6.pack(side=LEFT)
But6.pack(padx=30)
But6.pack(pady=10)
But7 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But7.pack(side=LEFT)
But7.pack(padx=30)
But7.pack(pady=10)
But8 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But8.pack(side=BOTTOM)
But8.pack(padx=0)
But8.pack(pady=0)
But9 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But9.pack(side=BOTTOM)
But9.pack(padx=0)
But9.pack(pady=0)
But10 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But10.pack(side=BOTTOM)
But10.pack(padx=0)
But10.pack(pady=0)
But11 = Frame(root, width=50, height=50, bd=2, relief=SOLID)
But11.pack(side=BOTTOM)
But11.pack(padx=0)
But11.pack(pady=0)
#================================LABEL WIDGETS==================================
#================================LABEL WIDGETS==================================
lbl_title = Label(Top, text="KoronaLab", width=600, font=("arial", 20))
lbl_title.pack(fill=X)
lbl_text0 = Label(But0, text="MM GRID", font=("arial", 30))
lbl_text0.bind("<Button-1>", LoadImage0)
lbl_text0.pack()
lbl_text1 = Label(But1, text="1", font=("arial", 25))
lbl_text1.bind("<Button-1>", lambda _:  LoadImage1(0))
lbl_text1.pack()
lbl_text2 = Label(But2, text="2", font=("arial", 25))
lbl_text2.bind("<Button-1>", lambda _: LoadImage1(1))
lbl_text2.pack()
lbl_text3 = Label(But3, text="3", font=("arial", 25))
lbl_text3.bind("<Button-1>", lambda _: LoadImage1(2))
lbl_text3.pack()
lbl_text4 = Label(But4, text="4", font=("arial", 25))
lbl_text4.bind("<Button-1>", lambda _: LoadImage1(3))
lbl_text4.pack()
lbl_text5 = Label(But5, text="5", font=("arial", 25))
lbl_text5.bind("<Button-1>", lambda _: LoadImage1(4))
lbl_text5.pack()
lbl_text6 = Label(But6, text="6", font=("arial", 25))
lbl_text6.bind("<Button-1>", lambda _: LoadImage1(5))
lbl_text6.pack()
lbl_text7 = Label(But7, text="7", font=("arial", 25))
lbl_text7.bind("<Button-1>", lambda _: LoadImage1(6))
lbl_text7.pack()
lbl_text8 = Label(But8, text="Mic1", font=("arial", 20))
lbl_text8.bind("<Button-1>", lambda _: SetMicro(0.7))
lbl_text8.pack()
lbl_text9 = Label(But9, text="Mic2", font=("arial", 20))
lbl_text9.bind("<Button-1>", lambda _: SetMicro(1.2))
lbl_text9.pack()
lbl_text10 = Label(But10, text="Mic3", font=("arial", 20))
lbl_text10.bind("<Button-1>", lambda _: SetMicro(0.95))
lbl_text10.pack()
lbl_text11 = Label(But11, text="Mic4", font=("arial", 20))
lbl_text11.bind("<Button-1>", lambda _: SetMicro(1.4))
lbl_text11.pack()


#================================INITIALIZATION=================================
if __name__ == '__main__':
    root.mainloop()