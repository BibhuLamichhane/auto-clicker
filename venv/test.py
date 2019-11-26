# declarations
from tkinter import *
import tkinter
import time
from pynput.keyboard import *
from tkinter import ttk
keyboard = Controller()
row_counter =140
c =1
commands = []
pauseTime = []


def lc():
    global v
    if v.get()==1:
     return v


def rc():
    global v
    if v.get() == 2:
     return v


def lettera():
    global v
    if v.get() == 3:
     return v


def letterb():
    global v
    if v.get() == 4:
     return v


def letterc():
    global v
    if v.get() == 5:
     return v


def letterd():
    global v
    if v.get() == 6:
     return v


def lettere():
    global v
    if v.get() == 7:
     return v


def letterf():
    global v
    if v.get() == 8:
     return v


def letterg():
    global v
    if v.get() == 9:
     return v


def letterh():
    global v
    if v.get() == 10:
     return v


def letteri():
    global v
    if v.get() == 11:
     return v


def letterj():
    global v
    if v.get() == 12:
     return v


def letterk():
    global v
    if v.get() == 13:
     return v


def letterl():
    global v
    if v.get() == 14:
     return v


def letterm():
    global v
    if v.get() == 15:
     return v


def lettern():
    global v
    if v.get() == 16:
     return v


def lettero():
    global v
    if v.get() == 17:
     return v


def letterp():
    global v
    if v.get() == 18:
     return v


def letterq():
    global v
    if v.get() == 19:
     return v


def letterr():
    global v
    if v.get() == 20:
     return v


def letters():
    global v
    if v.get() == 21:
     return v


def lettert():
    global v
    if v.get() == 22:
     return v


def letteru():
    global v
    if v.get() == 23:
     return v


def letterv():
    global v
    if v.get() == 24:
     return v


def letterw():
    global v
    if v.get() ==25:
     return v


def letterx():
    global v
    if v.get() == 26:
     return v


def lettery():
    global v
    if v.get() == 27:
     return v


def letterz():
    global v
    if v.get() == 28:
     return v


def num0():
    global v
    if v.get() == 29:
     return v


def num1():
    global v
    if v.get() == 30:
     return v


def num2():
    global v
    if v.get() == 31:
     return v


def num3():
    global v
    if v.get() == 32:
     return v


def num4():
    global v
    if v.get() == 33:
     return v


def num5():
    global v
    if v.get() == 34:
     return v


def num6():
    global v
    if v.get() == 35:
     return v


def num7():
    global v
    if v.get() == 36:
     return v


def num8():
    global v
    if v.get() == 37:
     return v


def num9():
    global v
    if v.get() == 38:
     return v


def main_outputInstruction():
 global c
 global a
 if v.get() ==1:
     o = int(pause_time.get())
     commands.append("lc")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press left click and pause for {o} seconds")
 if v.get() ==2:
     o = int(pause_time.get())
     commands.append("rc")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press right click and pause for {o} seconds")
 if v.get() ==3:
     o = int(pause_time.get())
     commands.append("a")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'a' and pause for {o} seconds")
 if v.get() == 4:
     o = int(pause_time.get())
     commands.append("b")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END, f"Press 'b' and pause for {o} seconds")
 if v.get() ==5:
     o = int(pause_time.get())
     commands.append("c")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'c' and pause for {o} seconds")
 if v.get() ==6:
     o = int(pause_time.get())
     commands.append("d")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'd' and pause for {o} seconds")
 if v.get() ==7:
     o = int(pause_time.get())
     commands.append("e")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'e' and pause for {o} seconds")
 if v.get() ==8:
     o = int(pause_time.get())
     commands.append("f")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'f' and pause for {o} seconds")
 if v.get() ==9:
     o = int(pause_time.get())
     commands.append("g")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'g' and pause for {o} seconds")
 if v.get() ==10:
     o = int(pause_time.get())
     commands.append("h")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'h' and pause for {o} seconds")
 if v.get() ==11:
     o = int(pause_time.get())
     commands.append("i")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'i' and pause for {o} seconds")
 if v.get() ==12:
     o = int(pause_time.get())
     commands.append("j")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'j' and pause for {o} seconds")
 if v.get() ==13:
     o = int(pause_time.get())
     commands.append("k")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'k' and pause for {o} seconds")
 if v.get() ==14:
     o = int(pause_time.get())
     commands.append("l")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'l' and pause for {o} seconds")
 if v.get() ==15:
     o = int(pause_time.get())
     commands.append("m")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'm' and pause for {o} seconds")
 if v.get() ==16:
     o = int(pause_time.get())
     commands.append("n")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'n' and pause for {o} seconds")
 if v.get() ==17:
     o = int(pause_time.get())
     commands.append("o")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'o' and pause for {o} seconds")
 if v.get() ==18:
     o = int(pause_time.get())
     commands.append("p")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'p' and pause for {o} seconds")
 if v.get() ==19:
     o = int(pause_time.get())
     commands.append("q")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'q' and pause for {o} seconds")
 if v.get() ==20:
     o = int(pause_time.get())
     commands.append("r")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'r' and pause for {o} seconds")
 if v.get() ==21:
     o = int(pause_time.get())
     commands.append("s")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 's' and pause for {o} seconds")
 if v.get() ==22:
     o = int(pause_time.get())
     commands.append("t")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 't' and pause for {o} seconds")
 if v.get() ==23:
     o = int(pause_time.get())
     commands.append("u")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'u' and pause for {o} seconds")
 if v.get() ==24:
     o = int(pause_time.get())
     commands.append("v")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'v' and pause for {o} seconds")
 if v.get() ==25:
     o = int(pause_time.get())
     commands.append("w")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'w' and pause for {o} seconds")
 if v.get() ==26:
     o = int(pause_time.get())
     commands.append("x")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'x' and pause for {o} seconds")
 if v.get() ==27:
     o = int(pause_time.get())
     commands.append("y")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'y' and pause for {o} seconds")
 if v.get() ==28:
     o = int(pause_time.get())
     commands.append("z")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press 'z' and pause for {o} seconds")
 if v.get() ==29:
     o = int(pause_time.get())
     commands.append("0")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press '0' and pause for {o} seconds")
 if v.get() ==30:
     o = int(pause_time.get())
     commands.append("1")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press '1' and pause for {o} seconds")
 if v.get() ==31:
     o = int(pause_time.get())
     commands.append("2")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press '2' and pause for {o} seconds")
 if v.get() ==32:
     o = int(pause_time.get())
     commands.append("3")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press '3' and pause for {o} seconds")
 if v.get() ==33:
     o = int(pause_time.get())
     commands.append("4")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press '4' and pause for {o} seconds")
 if v.get() ==34:
     o = int(pause_time.get())
     commands.append("5")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press '5' and pause for {o} seconds")
 if v.get() ==35:
     o = int(pause_time.get())
     commands.append("6")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press '6' and pause for {o} seconds")
 if v.get() ==36:
     o = int(pause_time.get())
     commands.append("7")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press '7' and pause for {o} seconds")
 if v.get() ==37:
     o = int(pause_time.get())
     commands.append("8")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press '8' and pause for {o} seconds")
 if v.get() ==38:
     o = int(pause_time.get())
     commands.append("9")
     pauseTime.append(o)
     for line in range(1):
      mylist.insert(END,f"Press '9' and pause for {o} seconds")
 print(commands)
 print(pauseTime)
 c =c+1
 mylist.place(x=0, y=180)

















# main screen
main_screen = Tk()
main_screen.title("Auto Clicker")
main_screen.geometry("500x645")
Button(main_screen,text="Start",width = 20 , height =3,bg = "grey",font = "19" ).place(x=145,y=559)
main_screen.resizable(False, False)
sb = Scrollbar(main_screen)
sb.pack(side=RIGHT, fill=Y)
mylist = Listbox(main_screen, yscrollcommand=sb.set, width=80, height=23)
sb.config(command=mylist.yview)

# main tab
tabs = ttk.Notebook(main_screen)

# mouse
Mouse_Clicks = ttk.Frame(tabs)
tabs.add(Mouse_Clicks, text='Mouse Clicker')
v=tkinter.IntVar()
btn = Radiobutton(Mouse_Clicks, text="Left Click", font="1", variable=v, value=1,command=lc)
btn.pack(anchor=W)
btn2 = Radiobutton(Mouse_Clicks, text="Right Click", font="1",  variable=v, value=2,command =rc)
btn2.pack(anchor="w")
lb1=Label(main_screen, text="Input the pause between the clicks (1 = 1 sec)" )
lb1.place(x=0,y=95)
pause_time = Entry(main_screen, width=10 )
pause_time.place(x=0,y=114)
lb2=Label(main_screen, text="Enter a numeric value",fg="red" )
lb2.place(x=0,y=133)
btn3=Button(main_screen,text = "Add command" ,command = main_outputInstruction)
btn3.place(x=0,y=157)




# alphabets
Alphabets = ttk.Frame(tabs)
tabs.add(Alphabets, text='Alphabets')
btn = Radiobutton(Alphabets, text="a",  variable=v, value=3,command=lettera)
btn.place(x=0,y=0)
btn = Radiobutton(Alphabets, text="b",  variable=v, value=4,command=letterb)
btn.place(x=28,y=0)
btn = Radiobutton(Alphabets, text="c",  variable=v, value=5,command=letterc)
btn.place(x=58,y=0)
btn = Radiobutton(Alphabets, text="d",  variable=v, value=6,command=letterd)
btn.place(x=88,y=0)
btn = Radiobutton(Alphabets, text="e",  variable=v, value=7,command=lettere)
btn.place(x=118,y=0)
btn = Radiobutton(Alphabets, text="f",  variable=v, value=8,command=letterf)
btn.place(x=148,y=0)
btn = Radiobutton(Alphabets, text="g",  variable=v, value=9,command=letterg)
btn.place(x=178,y=0)
btn = Radiobutton(Alphabets, text="h",  variable=v, value=10,command=letterh)
btn.place(x=208,y=0)
btn = Radiobutton(Alphabets, text="i",  variable=v, value=11,command=letteri)
btn.place(x=238,y=0)
btn = Radiobutton(Alphabets, text="j",  variable=v, value=12,command=letterj)
btn.place(x=268,y=0)
btn = Radiobutton(Alphabets, text="k",  variable=v, value=13,command=letterk)
btn.place(x=298,y=0)
btn = Radiobutton(Alphabets, text="l",  variable=v, value=14,command=letterl)
btn.place(x=328,y=0)
btn = Radiobutton(Alphabets, text="m",  variable=v, value=15,command=letterm)
btn.place(x=358,y=0)
btn = Radiobutton(Alphabets, text="n",  variable=v, value=16,command=lettern)
btn.place(x=393,y=0)
btn = Radiobutton(Alphabets, text="o",  variable=v, value=17,command=lettero)
btn.place(x=423,y=0)
btn = Radiobutton(Alphabets, text="p",  variable=v, value=18,command=letterp)
btn.place(x=0,y=25)
btn = Radiobutton(Alphabets, text="q",  variable=v, value=19,command=letterq)
btn.place(x=30,y=25)
btn = Radiobutton(Alphabets, text="r",  variable=v, value=20,command=letterr)
btn.place(x=60,y=25)
btn = Radiobutton(Alphabets, text="s",  variable=v, value=21,command=letters)
btn.place(x=90,y=25)
btn = Radiobutton(Alphabets, text="t",  variable=v, value=22,command=lettert)
btn.place(x=120,y=25)
btn = Radiobutton(Alphabets, text="u",  variable=v, value=23,command=letteru)
btn.place(x=150,y=25)
btn = Radiobutton(Alphabets, text="v",  variable=v, value=24,command=letterv)
btn.place(x=180,y=25)
btn = Radiobutton(Alphabets, text="w",  variable=v, value=25,command=letterw)
btn.place(x=210,y=25)
btn = Radiobutton(Alphabets, text="x",  variable=v, value=26,command=letterx)
btn.place(x=243,y=25)
btn = Radiobutton(Alphabets, text="y",  variable=v, value=27,command=lettery)
btn.place(x=273,y=25)
btn = Radiobutton(Alphabets, text="z",  variable=v, value=28,command=letterz)
btn.place(x=303,y=25)

# numbers
Numbers = ttk.Frame(tabs)
tabs.add(Numbers, text='Numbers')
btn = Radiobutton(Numbers, text="0",  variable=v, value=29,command=num0)
btn.place(x=0,y=0)
btn = Radiobutton(Numbers, text="1",  variable=v, value=30,command=num1)
btn.place(x=0,y=25)
btn = Radiobutton(Numbers, text="2",  variable=v, value=31,command=num2)
btn.place(x=30,y=0)
btn = Radiobutton(Numbers, text="3",  variable=v, value=32,command=num3)
btn.place(x=30,y=25)
btn = Radiobutton(Numbers, text="4",  variable=v, value=33,command=num4)
btn.place(x=58,y=0)
btn = Radiobutton(Numbers, text="5",  variable=v, value=34,command=num5)
btn.place(x=58,y=25)
btn = Radiobutton(Numbers, text="6",  variable=v, value=35,command=num6)
btn.place(x=88,y=0)
btn = Radiobutton(Numbers, text="7",  variable=v, value=36,command=num7)
btn.place(x=88,y=25)
btn = Radiobutton(Numbers, text="8",  variable=v, value=37,command=num8)
btn.place(x=118,y=0)
btn = Radiobutton(Numbers, text="9",  variable=v, value=38,command=num9)
btn.place(x=118,y=25)

# Symbols
Symbols = ttk.Frame(tabs)
tabs.add(Symbols,text ='Symbols')
btn = Radiobutton(Symbols, text="?",  variable=v, value=67,command=num0)
btn.place(x=0,y=0)
btn = Radiobutton(Symbols, text="@",  variable=v, value=39,command=num0)
btn.place(x=30,y=0)
btn = Radiobutton(Symbols, text="!",  variable=v, value=40,command=num0)
btn.place(x=63,y=0)
btn = Radiobutton(Symbols, text="#",  variable=v, value=41,command=num0)
btn.place(x=93,y=0)
btn = Radiobutton(Symbols, text="$",  variable=v, value=42,command=num0)
btn.place(x=123,y=0)
btn = Radiobutton(Symbols, text="%",  variable=v, value=43,command=num0)
btn.place(x=153,y=0)
btn = Radiobutton(Symbols, text="^",  variable=v, value=44,command=num0)
btn.place(x=183,y=0)
btn = Radiobutton(Symbols, text="&",  variable=v, value=45,command=num0)
btn.place(x=213,y=0)
btn = Radiobutton(Symbols, text="*",  variable=v, value=46,command=num0)
btn.place(x=243,y=0)
btn = Radiobutton(Symbols, text="(",  variable=v, value=47,command=num0)
btn.place(x=273,y=0)
btn = Radiobutton(Symbols, text=")",  variable=v, value=48,command=num0)
btn.place(x=303,y=0)
btn = Radiobutton(Symbols, text="-",  variable=v, value=49,command=num0)
btn.place(x=333,y=0)
btn = Radiobutton(Symbols, text="_",  variable=v, value=50,command=num0)
btn.place(x=363,y=0)
btn = Radiobutton(Symbols, text="=",  variable=v, value=51,command=num0)
btn.place(x=393,y=0)
btn = Radiobutton(Symbols, text="+",  variable=v, value=52,command=num0)
btn.place(x=413,y=0)
btn = Radiobutton(Symbols, text="[",  variable=v, value=67,command=num0)
btn.place(x=0,y=25)
btn = Radiobutton(Symbols, text="]",  variable=v, value=39,command=num0)
btn.place(x=30,y=25)
btn = Radiobutton(Symbols, text="{",  variable=v, value=40,command=num0)
btn.place(x=63,y=25)
btn = Radiobutton(Symbols, text="}",  variable=v, value=41,command=num0)
btn.place(x=93,y=25)
btn = Radiobutton(Symbols, text=";",  variable=v, value=42,command=num0)
btn.place(x=123,y=25)
btn = Radiobutton(Symbols, text=":",  variable=v, value=43,command=num0)
btn.place(x=153,y=25)
btn = Radiobutton(Symbols, text="'",  variable=v, value=44,command=num0)
btn.place(x=183,y=25)
btn = Radiobutton(Symbols, text='"',  variable=v, value=45,command=num0)
btn.place(x=213,y=25)
btn = Radiobutton(Symbols, text="\\",  variable=v, value=46,command=num0)
btn.place(x=243,y=25)
btn = Radiobutton(Symbols, text="|",  variable=v, value=47,command=num0)
btn.place(x=273,y=25)
btn = Radiobutton(Symbols, text="<",  variable=v, value=48,command=num0)
btn.place(x=303,y=25)
btn = Radiobutton(Symbols, text=">",  variable=v, value=49,command=num0)
btn.place(x=333,y=25)
btn = Radiobutton(Symbols, text=",",  variable=v, value=50,command=num0)
btn.place(x=363,y=25)
btn = Radiobutton(Symbols, text=".",  variable=v, value=51,command=num0)
btn.place(x=393,y=25)
btn = Radiobutton(Symbols, text="/",  variable=v, value=52,command=num0)
btn.place(x=413,y=25)
tabs.pack(fill=X)
main_screen.mainloop()
