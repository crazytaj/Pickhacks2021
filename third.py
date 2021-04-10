import tkinter as tk
from tkinter import ttk
import keyboard
import time
from PIL import Image, ImageTk

FILENAME = 'keyboard.png'

key = tk.Tk()  # key window name
key.title('Keyboard')  # title Name
    # icon add

keyboardpic = Image.open(FILENAME)

panel1 = tk.Label(key, image=ImageTk.PhotoImage(keyboardpic))
panel1.grid(row = 0, column = 2, sticky='E')

'''canvas = tk.Canvas(key, width = 1030, height = 670)
tk_img = ImageTk.PhotoImage(file = FILENAME)
canvas.create_image(125, 125, image = tk_img)'''

def press(src):

    keyboard.start_recording()
    time.sleep(1)
    gen = keyboard.stop_recording()

    bind = str(list(keyboard.get_typed_strings(gen)))[2].lower()

    if bind == "'":
        pass
    else:
        keyboard.remap_key(src, bind)
        variables[corresponding_str.index(src)].config(text=bind.upper())

    key.update()

def switch(src):

    Dis_entry.insert(0, 'Press the keys you would like to switch.')
    keys = []

    Dis_entry.delete('0', 'end')


    keyboard.start_recording()
    time.sleep(3)
    its = keyboard.stop_recording()

    if len(list(its)) != 4:
        Dis_entry.insert(0, 'Sorry, there was an error. Make sure you only type 2 keys, one after the other.')

    else:
        itss = list(keyboard.get_typed_strings(its))
        print(f'ok good here: {itss}')
        [[keys.append(letter) for letter in letra] for letra in itss]

        print(keys)

    keyboard.remap_key(keys[0], keys[1])
    keyboard.remap_key(keys[1], keys[0])

    variables[corresponding_str.index(keys[0].upper())].config(text = keys[1].upper())
    variables[corresponding_str.index(keys[1].upper())].config(text = keys[0].upper())



# Size window size
key.geometry('1050x300')         # normal size
key.maxsize(width=1920, height=1080)      # maximum size
key.minsize(width= 1100 , height = 300)     # minimum size
# end window size

key.configure(bg = 'green')    #  add background color

# entry box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key,state= 'readandwrite',textvariable = equation)
Dis_entry.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)
# end entry box

# add all button line wise 

# First Line Button

Switch = ttk.Button(key, text = 'If you want to switch two keys, click here', command = lambda : switch('test'))
Switch.grid(row = 5, columnspan = 4, ipadx = 6, ipady = 10)
Switch.lift()

Q = ttk.Button(key,text = 'Q' , width = 6, command = lambda : press('Q'))
Q.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)
Q.lift()

W = ttk.Button(key,text = 'W' , width = 6, command = lambda : press('W'))
W.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)
W.lift()

E = ttk.Button(key,text = 'E' , width = 6, command = lambda : press('E'))
E.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)
E.lift()

R = ttk.Button(key,text = 'R' , width = 6, command = lambda : press('R'))
R.grid(row = 1 , column = 3, ipadx = 6 , ipady = 10)
R.lift()

T = ttk.Button(key,text = 'T' , width = 6, command = lambda : press('T'))
T.grid(row = 1 , column = 4, ipadx = 6 , ipady = 10)
T.lift()

Y = ttk.Button(key,text = 'Y' , width = 6, command = lambda : press('Y'))
Y.grid(row = 1 , column = 5, ipadx = 6 , ipady = 10)
Y.lift()

U = ttk.Button(key,text = 'U' , width = 6, command = lambda : press('U'))
U.grid(row = 1 , column = 6, ipadx = 6 , ipady = 10)
U.lift()

I = ttk.Button(key,text = 'I' , width = 6, command = lambda : press('I'))
I.grid(row = 1 , column = 7, ipadx = 6 , ipady = 10)
I.lift()

O = ttk.Button(key,text = 'O' , width = 6, command = lambda : press('O'))
O.grid(row = 1 , column = 8, ipadx = 6 , ipady = 10)
O.lift()

P = ttk.Button(key,text = 'P' , width = 6, command = lambda : press('P'))
P.grid(row = 1 , column = 9, ipadx = 6 , ipady = 10)
P.lift()

cur = ttk.Button(key,text = '{' , width = 6, command = lambda : press('{'))
cur.grid(row = 1 , column = 10 , ipadx = 6 , ipady = 10)
cur.lift()

cur_c = ttk.Button(key,text = '}' , width = 6, command = lambda : press('}'))
cur_c.grid(row = 1 , column = 11, ipadx = 6 , ipady = 10)
cur_c.lift()

back_slash = ttk.Button(key,text = '\\' , width = 6, command = lambda : press('\\'))
back_slash.grid(row = 1 , column = 12, ipadx = 6 , ipady = 10)
back_slash.lift()

def clear():
    pass

clear = ttk.Button(key,text = 'Clear' , width = 6, command = clear)
clear.grid(row = 1 , column = 13, ipadx = 20 , ipady = 10)

# Second Line Button



A = ttk.Button(key,text = 'A' , width = 6, command = lambda : press('A'))
A.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)
A.lift()

S = ttk.Button(key,text = 'S' , width = 6, command = lambda : press('S'))
S.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)
S.lift()

D = ttk.Button(key,text = 'D' , width = 6, command = lambda : press('D'))
D.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)
D.lift()

F = ttk.Button(key,text = 'F' , width = 6, command = lambda : press('F'))
F.grid(row = 2 , column = 3, ipadx = 6 , ipady = 10)
F.lift()


G = ttk.Button(key,text = 'G' , width = 6, command = lambda : press('G'))
G.grid(row = 2 , column = 4, ipadx = 6 , ipady = 10)
G.lift()


H = ttk.Button(key,text = 'H' , width = 6, command = lambda : press('H'))
H.grid(row = 2 , column = 5, ipadx = 6 , ipady = 10)
H.lift()

J = ttk.Button(key,text = 'J' , width = 6, command = lambda : press('J'))
J.grid(row = 2 , column = 6, ipadx = 6 , ipady = 10)
J.lift()

K = ttk.Button(key,text = 'K' , width = 6, command = lambda : press('K'))
K.grid(row = 2 , column = 7, ipadx = 6 , ipady = 10)
K.lift()

L = ttk.Button(key,text = 'L' , width = 6, command = lambda : press('L'))
L.grid(row = 2 , column = 8, ipadx = 6 , ipady = 10)
L.lift()

semi_co = ttk.Button(key,text = ';' , width = 6, command = lambda : press(';'))
semi_co.grid(row = 2 , column = 9, ipadx = 6 , ipady = 10)
semi_co.lift()

d_colon = ttk.Button(key,text = '"' , width = 6, command = lambda : press('"'))
d_colon.grid(row = 2 , column = 10, ipadx = 6 , ipady = 10)
d_colon.lift()

def action():
    pass

enter = ttk.Button(key,text = 'Enter' , width = 6, command = action)
enter.grid(row = 2 , columnspan = 75, ipadx = 85 , ipady = 10)
enter.lift()

# third line Button

Z = ttk.Button(key,text = 'Z' , width = 6, command = lambda : press('Z'))
Z.grid(row = 3 , column = 0, ipadx = 6 , ipady = 10)
Z.lift()

X = ttk.Button(key,text = 'X' , width = 6, command = lambda : press('X'))
X.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)
X.lift()

C = ttk.Button(key,text = 'C' , width = 6, command = lambda : press('C'))
C.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)
C.lift()

V = ttk.Button(key,text = 'V' , width = 6, command = lambda : press('V'))
V.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)
V.lift()

B = ttk.Button(key, text= 'B' , width = 6 , command = lambda : press('B'))
B.grid(row = 3 , column = 4 , ipadx = 6 ,ipady = 10)
B.lift()

N = ttk.Button(key,text = 'N' , width = 6, command = lambda : press('N'))
N.grid(row = 3 , column = 5, ipadx = 6 , ipady = 10)
N.lift()

M = ttk.Button(key,text = 'M' , width = 6, command = lambda : press('M'))
M.grid(row = 3 , column = 6, ipadx = 6 , ipady = 10)
M.lift()

left = ttk.Button(key,text = '<' , width = 6, command = lambda : press('<'))
left.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)
left.lift()

right = ttk.Button(key,text = '>' , width = 6, command = lambda : press('>'))
right.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)
right.lift()

slas = ttk.Button(key,text = '/' , width = 6, command = lambda : press('/'))
slas.grid(row = 3 , column = 9, ipadx = 6 , ipady = 10)
slas.lift()

q_mark = ttk.Button(key,text = '?' , width = 6, command = lambda : press('?'))
q_mark.grid(row = 3 , column = 10, ipadx = 6 , ipady = 10)
q_mark.lift()

coma = ttk.Button(key,text = ',' , width = 6, command = lambda : press(','))
coma.grid(row = 3 , column = 11, ipadx = 6 , ipady = 10)
coma.lift()

dot = ttk.Button(key,text = '.' , width = 6, command = lambda : press('.'))
dot.grid(row = 3 , column = 12, ipadx = 6 , ipady = 10)
dot.lift()

shift = ttk.Button(key,text = 'Shift' , width = 6, command = lambda : press('Shift'))
shift.grid(row = 3 , column = 13, ipadx = 20 , ipady = 10)
shift.lift()

#Fourth Line Button


ctrl = ttk.Button(key,text = 'Ctrl' , width = 6, command = lambda : press('Ctrl'))
ctrl.grid(row = 4 , column = 0, ipadx = 6 , ipady = 10)
ctrl.lift()

Fn = ttk.Button(key,text = 'Fn' , width = 6, command = lambda : press('Fn'))
Fn.grid(row = 4 , column = 1, ipadx = 6 , ipady = 10)
Fn.lift()

window = ttk.Button(key,text = 'Window' , width = 6, command = lambda : press('Window'))
window.grid(row = 4 , column = 2 , ipadx = 6 , ipady = 10)
window.lift()

Alt = ttk.Button(key,text = 'Alt' , width = 6, command = lambda : press('Alt'))
Alt.grid(row = 4 , column = 3 , ipadx = 6 , ipady = 10)
Alt.lift()

space = ttk.Button(key,text = 'Space' , width = 6, command = lambda : press(' '))
space.grid(row = 4 , columnspan = 14 , ipadx = 160 , ipady = 10)
space.lift()

Alt_gr = ttk.Button(key,text = 'Alt Gr' , width = 6, command = lambda : press('Alt Gr'))
Alt_gr.grid(row = 4 , column = 10 , ipadx = 6 , ipady = 10)
Alt_gr.lift()

open_b = ttk.Button(key,text = '(' , width = 6, command = lambda : press('('))
open_b.grid(row = 4 , column = 11 , ipadx = 6 , ipady = 10)
open_b.lift()

close_b = ttk.Button(key,text = ')' , width = 6, command = lambda : press(')'))
close_b.grid(row = 4 , column = 12 , ipadx = 6 , ipady = 10)
close_b.lift()

variables = [Q, W, E, R, T, Y, U, I, O, P, cur, cur_c, back_slash, A, S, D, F, G, H, J, K, L, semi_co, d_colon, Z, X, C, V, B, N, M,
             left, right, slas, q_mark, coma, dot, shift, ctrl, Fn, window, Alt, space, Alt_gr, open_b, close_b,]

corresponding_str = ['Q','W','E','R','T','Y','U','I','O','P','{','}','\\','A','S','D','F','G','H','J',
                     'K','L',';', '"','Z','X','C','V','B','N','M','<','>','/','?',',','.','Shift','Ctrl',
                     'Fn','Window','Alt',' ','Alt Gr','(',')']

def Tab():
    pass
tap = ttk.Button(key,text = 'Tab' , width = 6, command = Tab)
tap.grid(row = 4 , column = 13 , ipadx = 20 , ipady = 10)


key.mainloop()
keyboard.wait('ctrl+shift+l')


